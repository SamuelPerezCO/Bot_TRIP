# async def main():
#     await client.send_message('@cabezonbebe', 'Hello! Talking to you from Telethon')
#     await client.send_file('@cabezonbebe', '/home/samuelp/Pictures/UNP/ChatGPT Image Feb 5, 2026, 10_35_16 PM.png')

#     messages = await client.get_messages('@cabezonbebe')
#     if messages:
#         await messages[0].download_media()

#     print("Bot is running. Listening for 'hi/hello' messages...")
#     await client.run_until_disconnected()
#     1. Run the member‑fetching function from save_user
#     await get_members(client, 'Estudiantes Academia de Idiomas Smart')
#     await get_members(client, 'Test')
    
#     2. Optional: send a test message / file
#     await client.send_message('@cabezonbebe', 'Hello! Talking to you from Telethon')
#     await client.send_file('@cabezonbebe', '/home/sample/Pictures/UNP/chat.png')
    
#     3. Fetch recent messages (optional)
#     messages = await client.get_messages('@cabezonbebe', limit=5)
#     for msg in messages:
#         print(f"Msg: {msg.text}")
    
#     print("Bot is running. Listening for 'hi/hello' messages...")
#     await client.run_until_disconnected()   

# @client.on(events.NewMessage(pattern='(?i)hi|hello'))
# async def handler(event):
#     print(f"Received: {event.message.text}")
#     await event.respond('Hey!')