import os

from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

phone = os.getenv("TELEGRAM_PHONE_NUMBER")
session_file = os.getenv("TELEGRAM_USERNAME")
password = os.getenv("TELEGRAM_PASSWORD")

client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True).start(phone, password)

message = "This is auto-reply. Please wait, I'll check it later."

@client.on(events.NewMessage)
async def auto_reply(event):
    if event.is_private:
        from_ = await event.client.get_entity(event.from_id)
        if not from_.bot:
            print(event.message)
            await event.reply(message)

def main():
    client.run_until_disconnected()

if __name__ == '__main__':
    print("Auto replying...")
    main()
