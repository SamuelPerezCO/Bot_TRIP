from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_API_ID = os.getenv("api_id")     # Telegram requires int
TELEGRAM_API_HASH = os.getenv("api_hash")

client = TelegramClient('TRIP_UNP_BOT', TELEGRAM_API_ID, TELEGRAM_API_HASH)

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    print(f"Received: {event.message.text}")
    await event.respond('Hey!')

async def main():
    # Optional: send a startup message / test file
    await client.send_message('@cabezonbebe', 'Hello! Talking to you from Telethon')
    await client.send_file('@cabezonbebe', '/home/samuelp/Pictures/UNP/ChatGPT Image Feb 5, 2026, 10_35_16 PM.png')

    # Download your own profile photo? (uncomment if needed)
    # await client.download_profile_photo('me')

    # Get recent messages and download media from the first one
    messages = await client.get_messages('@cabezonbebe')
    if messages:
        await messages[0].download_media()

    print("Bot is running. Listening for 'hi/hello' messages...")
    await client.run_until_disconnected()   # this keeps the bot alive

if __name__ == '__main__':
    client.start()
    client.loop.run_until_complete(main())