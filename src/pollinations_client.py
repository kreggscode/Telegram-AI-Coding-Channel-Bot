import urllib.parse
import requests


def generate_text(prompt: str) -> str:
    """Generate free-form text from Pollinations.ai."""
    encoded = urllib.parse.quote(prompt)
    url = f"https://text.pollinations.ai/{encoded}"
    resp = requests.get(url, timeout=30)
    if resp.status_code == 200:
        return resp.text.strip()
    return "AI generation failed. Please try again."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations based on prompt."""
    encoded = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded}"
