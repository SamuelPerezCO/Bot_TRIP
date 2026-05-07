from telethon import TelegramClient, events
from get_client import client
from save_user import get_members

#F*ck

async def main():
    await get_members(client)
    await client.run_until_disconnected()   

if __name__ == '__main__':
    client.start()
    client.loop.run_until_complete(main())