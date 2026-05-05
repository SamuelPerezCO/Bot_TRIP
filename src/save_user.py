from telethon import TelegramClient

user_id_txt = open("user_id.txt" , "a")

async def get_members(client: TelegramClient):
    try:
        channel = await client.get_entity(-1001196822184)
        i = 1
        async for user in client.iter_participants(channel):
            print(f"{i} -{user.id} - {user.first_name} - {user.username}")
            user_id_txt.write(f"{user.id}")
            i += 1
        user_id_txt.close()

    except Exception as e:
        print(f"Error fetching members: {e}")