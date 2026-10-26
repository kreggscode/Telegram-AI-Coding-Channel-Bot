import urllib.parse
import requests
import random
import time
from datetime import datetime
from .config import POLLINATIONS_API_KEY, AI_MODEL

SYSTEM_PROMPT = (
    "You are a Principal Software Architect and elite coding tutor creating educational content for developers on Telegram.\n"
    "CRITICAL FORMATTING & QUALITY DIRECTIVES:\n"
    "1. COMPLETE CODE: Whenever code is requested, provide a 100% complete, runnable, and bug-free production snippet. NEVER truncate code or use placeholders like '# ...' or '// todo'. Write genuine working logic.\n"
    "2. CODE BLOCKS: Always enclose all code in triple backticks with the lowercase language tag (e.g. ```python, ```javascript) so Telegram renders the syntax-highlighted Copy Code box.\n"
    "3. STRUCTURE: Use bold headers (**Header**), bullet points, and clean spacing for high visual readability.\n"
    "4. MATCHING DELIMITERS: Always ensure code blocks and markdown tags are properly opened and closed.\n"
    "5. QUIZ PRECISION: When a [QUIZ] is requested, place it at the very end strictly following the [QUIZ] ... [/QUIZ] format."
)


def generate_text(prompt: str) -> str:
    """Generate high-quality text using the paid Pollinations.ai API with intelligent fallback."""
    if not POLLINATIONS_API_KEY:
        print("CRITICAL: Pollinations API Key missing.")
        return "Pollinations API Key missing. Please check your config."

    seed = random.randint(1000, 999999)
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Enhanced prompt for better code and structured content
    enhanced_prompt = (
        f"{prompt}\n\n"
        f"STRICT INSTRUCTION: Provide elite, production-quality, non-truncated content. "
        f"Today's date: {date_str}. Seed: {seed}"
    )
    
    url = "https://gen.pollinations.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {POLLINATIONS_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Try with original model, then fallback to 'openai' or 'gemini-fast' if it fails
    models_to_try = [AI_MODEL, "openai", "gemini-fast"]
    # De-duplicate while preserving order
    seen = set()
    models_to_try = [m for m in models_to_try if not (m in seen or seen.add(m))]
    
    for model in models_to_try:
        attempts = 2
        for i in range(attempts):
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": enhanced_prompt}
                ],
                "seed": seed
            }
            
            try:
                print(f"LOG: AI Request (Model: {model}, Attempt: {i+1})...")
                resp = requests.post(url, headers=headers, json=payload, timeout=120)
                
                if resp.status_code == 200:
                    try:
                        data = resp.json()
                        content = data['choices'][0]['message']['content'].strip()
                        # Check if the content itself looks like an error message from Pollinations
                        if "AI generation failed" in content or "Please try again" in content:
                            print(f"WARNING: AI returned an error-like message: {content}")
                            continue
                        return content
                    except (ValueError, KeyError, IndexError) as e:
                        print(f"ERROR: Failed to parse AI JSON response: {e}. Raw: {resp.text[:200]}")
                        continue
                else:
                    print(f"ERROR: Pollinations API {resp.status_code} - {resp.text[:200]}")
                    if resp.status_code == 402:
                        return "API Error: Payment Required (No Pollen/Credits)."
                    if resp.status_code == 401:
                        return "API Error: Invalid API Key."
            except Exception as e:
                print(f"EXCEPTION during AI generation ({model}): {e}")
            
            if i < attempts - 1:
                time.sleep(2)
        
        print(f"LOG: Model {model} failed all attempts. Trying next model if available...")

    return "AI generation failed. Please check API status or credits."


def image_url(prompt: str, model: str = "flux") -> str:
    """Image generation DISABLED to stop Pollinations flux image costs."""
    print("--- POLLINATIONS IMAGE GENERATION DISABLED ---")
    return None
