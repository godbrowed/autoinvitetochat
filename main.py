import asyncio
import random
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

API_ID = your api_id 
API_HASH = "your api hash, find in my.telegram.org"
PHONE_NUMBER = "+number"
CHAT_ID = "yourchat"  

client = TelegramClient("userbot_session", API_ID, API_HASH)

async def invite_users():
    await client.start(PHONE_NUMBER)  

    while True: 
        with open("yourfile.txt", "r", encoding="utf-8") as file:
            usernames = [line.strip() for line in file if line.strip()]

        for username in usernames:
            try:
                await client(InviteToChannelRequest(CHAT_ID, [username]))
                print(f"✅ Invited: {username}")

                await asyncio.sleep(5)

            except Exception as e:
                print(f"❌ Error while inviting {username}: {e}")

        print("Aganin")
        await asyncio.sleep(5)

asyncio.run(invite_users())
