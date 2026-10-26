import sys
from src.formatter import markdown_to_telegram_html, plain_text_fallback_formatter, safe_truncate_html, split_telegram_html

test_cases = [
    (
        "Unclosed code block\n```python\nprint(1 < 2)",
        '<pre><code class="language-python">print(1 &lt; 2)</code></pre>'
    ),
    (
        "Inline `var_name` and `x < y`",
        "<code>var_name</code> and <code>x &lt; y</code>"
    ),
    (
        "[Instagram](https://instagram.com/kreggscode)",
        '<a href="https://instagram.com/kreggscode">Instagram</a>'
    ),
    (
        "**Bold Title** and *Italic subtitle*",
        "<b>Bold Title</b> and <i>Italic subtitle</i>"
    ),
    (
        "> Senior architectural tip",
        "<blockquote>Senior architectural tip</blockquote>"
    ),
    (
        "Multiple lines of code:\n```python\ndef test():\n    return 'hello & world'\n```",
        '<pre><code class="language-python">def test():\n    return \'hello &amp; world\'</code></pre>'
    )
]

for i, (inp, expected) in enumerate(test_cases):
    res = markdown_to_telegram_html(inp)
    assert expected in res, f"FAILED test case {i}: expected '{expected}' in '{res}'"

# Test plain text fallback
pt = plain_text_fallback_formatter("[Instagram](https://instagram.com/kreggscode)")
assert pt == "Instagram: https://instagram.com/kreggscode", f"Got: {pt}"

# Test safe truncation
long_html = "<b>" + ("A" * 5000) + "</b>"
truncated = safe_truncate_html(long_html, max_chars=100)
assert truncated.endswith("</b>"), f"Truncated didn't close tag: {truncated[-20:]}"

# Test split telegram html
mock_long_post = (
    "<b>🐍 Python Mastery: Day 250 - Concurrency</b>\n\n"
    "<b>💡 Architectural Insight:</b>\n" + ("Insight explanation text. " * 150) +
    "\n\n<b>💻 Production Code Snippet:</b>\n<pre><code class=\"language-python\">def solve():\n    return True</code></pre>\n\n"
    "<b>⚡ Key Takeaways:</b>\n• Pro-tip 1\n• Pro-tip 2"
)
splits = split_telegram_html(mock_long_post, max_chars=2000)
print(f"Long post ({len(mock_long_post)} chars) split into {len(splits)} parts:")
for idx, p in enumerate(splits):
    print(f"  Part {idx+1} length: {len(p)} chars")
    assert len(p) <= 2000, f"Part {idx+1} exceeds max_chars!"

print("All formatter tests including split_telegram_html PASSED!")
