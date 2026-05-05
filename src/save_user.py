from telethon import TelegramClient

async def get_members(client: TelegramClient):
    try:
        channel = await client.get_entity(-1001196822184)
        i = 0
        async for user in client.iter_participants(channel):
            # i+1 
            print(f"{i} -{user.id} - {user.first_name} - {user.username}")
    except Exception as e:
        print(f"Error fetching members: {e}")