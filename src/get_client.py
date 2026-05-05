from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_API_ID = os.getenv("api_id")
TELEGRAM_API_HASH = os.getenv("api_hash")

client = TelegramClient('TRIP_UNP_BOT' , TELEGRAM_API_ID , TELEGRAM_API_HASH)