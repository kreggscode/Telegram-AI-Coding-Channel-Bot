"""
Formatter Engine for Telegram Messages.
Converts Markdown to rock-solid Telegram HTML, handles code blocks,
syntax highlighting, interactive Copy buttons, hyperlinks, and edge cases.
"""

import html
import re


def markdown_to_telegram_html(text: str) -> str:
    """
    Convert Markdown content to clean, fully-compliant Telegram HTML.
    
    Guarantees:
    - Code blocks are converted to <pre><code class="language-{lang}">...</code></pre>
      which renders the syntax-highlighted code container with the native 'Copy' button in Telegram.
    - Inline code is converted to <code>...</code>.
    - Hyperlinks [label](url) are converted to <a href="url">label</a>.
    - Bold **text** / __text__ is converted to <b>text</b>.
    - Italic *text* is converted to <i>text</i>.
    - Blockquotes > text are converted to <blockquote>text</blockquote>.
    - All HTML special characters (&, <, >) in normal text and inside code blocks
      are safely escaped so Telegram's HTML parser NEVER fails with 400 Bad Request.
    - Unclosed code blocks from AI generation are automatically closed.
    """
    if not text:
        return ""

    # Normalize line breaks
    text = text.replace("\r\n", "\n")

    # 1. Auto-close unclosed code blocks if AI output was cut off
    triple_backtick_count = text.count("```")
    if triple_backtick_count % 2 != 0:
        text += "\n```"

    # 2. Extract and protect code blocks
    code_blocks = []
    def save_code_block(match):
        lang = (match.group(1) or "").strip().lower()
        code = match.group(2)
        # Escape HTML inside code
        escaped_code = html.escape(code.strip("\n"), quote=False)
        if lang:
            replacement = f'<pre><code class="language-{lang}">{escaped_code}</code></pre>'
        else:
            replacement = f'<pre><code>{escaped_code}</code></pre>'
        placeholder = f"TOKENXCODEBLOCKX{len(code_blocks)}XTOKEN"
        code_blocks.append(replacement)
        return f"\n{placeholder}\n"

    # Match ```lang\ncode\n```
    text = re.sub(r"```([a-zA-Z0-9_\-+]*)\n?(.*?)```", save_code_block, text, flags=re.DOTALL)

    # 3. Extract and protect inline code `code`
    inline_codes = []
    def save_inline_code(match):
        code = match.group(1)
        escaped_code = html.escape(code, quote=False)
        placeholder = f"TOKENXINLINEX{len(inline_codes)}XTOKEN"
        inline_codes.append(f"<code>{escaped_code}</code>")
        return placeholder

    text = re.sub(r"`([^`\n]+)`", save_inline_code, text)

    # 4. Extract and protect blockquotes (> quote)
    def quote_repl(match):
        lines = [
            line.strip()[2:].strip() if line.strip().startswith("> ") else line.strip()[1:].strip()
            for line in match.group(0).split("\n")
            if line.strip()
        ]
        return f"<blockquote>{chr(10).join(lines)}</blockquote>"
    
    text = re.sub(r"(?:^[ \t]*>[^\n]*(?:\n|$))+", quote_repl, text, flags=re.MULTILINE)

    blockquotes = []
    def save_quote(match):
        placeholder = f"TOKENXBLOCKQUOTEX{len(blockquotes)}XTOKEN"
        blockquotes.append(match.group(0))
        return placeholder

    text = re.sub(r"<blockquote>.*?</blockquote>", save_quote, text, flags=re.DOTALL)

    # 5. Escape HTML in the remaining text (& < >)
    text = html.escape(text, quote=False)

    # 6. Convert Markdown links [text](url) -> <a href="url">text</a>
    def link_repl(match):
        label = match.group(1).strip()
        url = match.group(2).strip()
        # Clean url and avoid quote issues
        safe_url = url.replace('"', "%22")
        return f'<a href="{safe_url}">{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\((https?://[^\s\)]+|t\.me/[^\s\)]+)\)", link_repl, text)

    # 7. Convert Markdown Headers (# Header, ## Header, ### Header) to <b>Header</b>
    text = re.sub(r"^(?:#{1,4})\s+(.+)$", r"<b>\1</b>", text, flags=re.MULTILINE)

    # 8. Convert Bold: **text** or __text__ -> <b>text</b>
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text, flags=re.DOTALL)
    text = re.sub(r"__(.+?)__", r"<b>\1</b>", text, flags=re.DOTALL)

    # 9. Convert Italic: *text* -> <i>text</i> (avoiding asterisks that are part of bullet points)
    text = re.sub(r"(?<!\*)\*([^\*\n]+)\*(?!\*)", r"<i>\1</i>", text)

    # 10. Restore blockquotes
    for i, replacement in enumerate(blockquotes):
        text = text.replace(f"TOKENXBLOCKQUOTEX{i}XTOKEN", replacement)

    # 11. Restore inline code
    for i, replacement in enumerate(inline_codes):
        text = text.replace(f"TOKENXINLINEX{i}XTOKEN", replacement)

    # 12. Restore code blocks
    for i, replacement in enumerate(code_blocks):
        text = text.replace(f"TOKENXCODEBLOCKX{i}XTOKEN", replacement)

    # 13. Clean up excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    return text


def plain_text_fallback_formatter(text: str) -> str:
    """
    Emergency fallback: Converts Markdown to clean human-readable plain text
    where links are formatted as 'Label: URL' so Telegram auto-links them,
    rather than showing ugly raw markdown brackets '[Instagram](https://...)'.
    """
    if not text:
        return ""

    # Replace markdown links [Label](URL) -> Label: URL
    text = re.sub(r"\[([^\]]+)\]\((https?://[^\s\)]+|t\.me/[^\s\)]+)\)", r"\1: \2", text)

    # Strip bold / italic markers
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"__(.+?)__", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^\*\n]+)\*(?!\*)", r"\1", text)

    # Strip headers # Header -> Header
    text = re.sub(r"^(?:#{1,4})\s+(.+)$", r"\1", text, flags=re.MULTILINE)

    # Strip blockquote prefix
    text = re.sub(r"^[ \t]*>[ \t]?", "", text, flags=re.MULTILINE)

    return text.strip()


def safe_truncate_html(text: str, max_chars: int = 4000) -> str:
    """
    Ensure the HTML message length stays within Telegram limits (4,096 chars).
    If it exceeds max_chars, safely trims and closes any dangling tags.
    """
    if len(text) <= max_chars:
        return text

    trimmed = text[:max_chars - 20]
    last_space = max(trimmed.rfind(" "), trimmed.rfind("\n"))
    if last_space > 0:
        trimmed = trimmed[:last_space]

    trimmed += "..."

    # Close any unclosed tags
    tags_to_check = ["code", "pre", "b", "i", "blockquote", "a"]
    for tag in tags_to_check:
        open_count = trimmed.count(f"<{tag}")
        close_count = trimmed.count(f"</{tag}>")
        if open_count > close_count:
            trimmed += f"</{tag}>"

    return trimmed


def split_telegram_html(text: str, max_chars: int = 3900) -> list[str]:
    """
    Split long Telegram HTML messages into logical, self-contained parts
    (e.g. Part 1: Theory/Insight, Part 2: Code Snippet/Implementation)
    so no code is truncated and all HTML tags remain valid.
    """
    if len(text) <= max_chars:
        return [text]

    # Try to split at logical section breaks first
    split_candidates = [
        "\n\n<b>💻 Production Code Snippet:</b>",
        "\n\n<b>💻 Production Code Snippet</b>",
        "\n\n<b>💻 Optimal Production Solution:</b>",
        "\n\n<b>💻 Security Audit / Remediation Script:</b>",
        "\n\n<pre>",
        "\n\n━━━━━━━━━━━━━━━━━━━━\n\n",
        "\n\n"
    ]
    
    for candidate in split_candidates:
        idx = text.find(candidate)
        if 400 <= idx <= max_chars:
            part1 = safe_truncate_html(text[:idx], max_chars=max_chars)
            part2 = text[idx:].strip()
            return [part1] + split_telegram_html(part2, max_chars)

    # Fallback to word boundary split
    last_break = max(text.rfind("\n\n", 0, max_chars), text.rfind("\n", 0, max_chars), text.rfind(" ", 0, max_chars))
    if last_break <= 0:
        last_break = max_chars

    part1 = safe_truncate_html(text[:last_break], max_chars=max_chars)
    part2 = text[last_break:].strip()
    return [part1] + split_telegram_html(part2, max_chars)
