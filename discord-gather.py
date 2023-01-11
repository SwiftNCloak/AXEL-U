import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    with open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/chatbot.txt', 'a') as f:
        f.write(f'\n\n{message.content}')

client.run('YOUR_BOT_TOKEN')