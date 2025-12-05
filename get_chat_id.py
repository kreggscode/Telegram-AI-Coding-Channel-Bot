"""
Quick script to get your Telegram Channel Chat ID
Run this after posting a message in your channel
"""

import requests

# Your bot token
BOT_TOKEN = "8255208641:AAHtbi2i80Ggx71f4wMwtvtlhBukhy9j_XQ"

print("🔍 Fetching updates from Telegram...\n")

# Get updates
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
response = requests.get(url)
data = response.json()

if not data.get("result"):
    print("❌ No updates found!")
    print("\n📝 TO FIX THIS:")
    print("1. Make sure your bot is added as ADMIN to your channel")
    print("2. Post a message in your channel")
    print("3. Forward that message to @userinfobot")
    print("4. Or try mentioning your bot in the channel: @your_bot_username")
    print("\n💡 EASIEST METHOD:")
    print("   Forward any channel message to @userinfobot or @RawDataBot")
else:
    print("✅ Found updates!\n")
    
    # Look for channel IDs
    channel_found = False
    for update in data["result"]:
        # Check different possible locations for chat info
        chat = None
        
        if "channel_post" in update:
            chat = update["channel_post"]["chat"]
        elif "message" in update:
            chat = update["message"]["chat"]
        elif "my_chat_member" in update:
            chat = update["my_chat_member"]["chat"]
        
        if chat and chat.get("type") == "channel":
            channel_found = True
            print(f"📢 Channel Found!")
            print(f"   Name: {chat.get('title', 'N/A')}")
            print(f"   ID: {chat['id']}")
            print(f"   Username: @{chat.get('username', 'N/A')}")
            print(f"\n✅ YOUR CHAT_ID: {chat['id']}")
            print(f"\n📋 Add this to your .env file:")
            print(f"   CHAT_ID={chat['id']}")
            print()
    
    if not channel_found:
        print("⚠️  No channel found in updates")
        print("\n💡 TRY THIS:")
        print("   Forward a message from your channel to @userinfobot")
        print("   It will show you the channel ID instantly!")

print("\n" + "="*60)
print("📚 Full API Response:")
print("="*60)
import json
print(json.dumps(data, indent=2))
