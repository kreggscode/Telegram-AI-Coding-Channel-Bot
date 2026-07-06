import os
os.environ['BOT_TOKEN'] = 'test_dummy_token_123456:ABCdefGHIJklmNOPqrSTUVwxyz'
os.environ['CHAT_ID'] = '-1001234567890'

from src.magazine_generator import create_magazine

print("=" * 60)
print("  GENERATING FULL MAGAZINE WITH AI CONTENT")
print("=" * 60)
print()

pdf_path = create_magazine()

print()
print(f"Magazine generated: {pdf_path}")
import os
print(f"File size: {os.path.getsize(pdf_path)} bytes")
print("Done!")
