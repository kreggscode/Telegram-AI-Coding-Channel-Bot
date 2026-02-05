import os
import sys
from dotenv import load_dotenv

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.magazine_generator import create_magazine
from src.telegram_client import send_document

def main():
    print("=== KREGGSCODE MAGAZINE TEST ===")
    try:
        pdf_path = create_magazine()
        print(f"Magazined generated: {pdf_path}")
        
        print("Sending to Telegram...")
        caption = "📖 *KREGGSCODE Daily Magazine*\n\nYour daily dose of Python, ML, and Code Architecture. Enjoy! 🚀"
        resp = send_document(pdf_path, caption=caption)
        
        if resp.status_code == 200:
            print("✅ Magazine sent successfully!")
        else:
            print(f"❌ Failed to send: {resp.status_code} - {resp.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
