import urllib.parse
import requests
import random
import time
from datetime import datetime
from .config import POLLINATIONS_API_KEY, AI_MODEL

def generate_text(prompt: str) -> str:
    """Generate high-quality text using the paid Pollinations.ai API with fallback."""
    if not POLLINATIONS_API_KEY:
        print("CRITICAL: Pollinations API Key missing.")
        return "Pollinations API Key missing. Please check your config."

    seed = random.randint(1000, 999999)
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Enhanced prompt for better code/tips
    enhanced_prompt = f"{prompt}\n\nIMPORTANT: Provide high-quality, professional, and unique content. Today's date: {date_str}. Seed: {seed}"
    
    url = "https://gen.pollinations.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {POLLINATIONS_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Try with original model, then fallback to 'openai' if it fails
    models_to_try = [AI_MODEL, "openai"]
    
    for model in models_to_try:
        attempts = 2
        for i in range(attempts):
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are a professional software engineer and coding tutor. Your goal is to provide insightful, accurate, and helpful coding tips, news, and explanations."},
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
                    print(f"ERROR: Pollinations API {resp.status_code} - {resp.text}")
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
