from telethon import TelegramClient , events , sync
from dotenv import load_dotenv
import sys
import os

load_dotenv()

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

client = TelegramClient('TRIP_UNP_BOT' , api_id = api_id , api_hash = api_hash)
client.start()

print(client.get_me().stringify())


client.send_message('@unaneaprogramadora' , 'Hello! Talking to you from Telethon')
client.send_file('@unaneaprogramadora' , '/home/samuelp/Pictures/UNP/ChatGPT Image Feb 5, 2026, 10_35_16 PM.png')

client.download_profile_photo('me')
messages = client.get_messages('@unaneaprogramadora')
messages[0].download_media()

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')
