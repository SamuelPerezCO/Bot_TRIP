from telethon import TelegramClient
from dotenv import load_dotenv
import sys
import os

load_dotenv()

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

client = TelegramClient('bot_trip' , api_id , api_hash)
