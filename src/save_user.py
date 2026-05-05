from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsSearch
from get_client import client

async def get_members():
    async with client:
        channel = await client.get_entity('Estudiantes Academia de Idiomas Smart')
        participants = await client.get_participants(channel)

        for user in participants:
            print(user.id , user.first_name , user.username)