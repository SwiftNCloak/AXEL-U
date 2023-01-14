import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    with open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/inputs.txt', 'a') as f:
        f.write(f'\n{message.content}')


@client.event
async def on_ready():
    print('AXEL-U is now activated')

    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'CHAT SYSTEM TESTING'
    ))

client.run('MTA2Mzc0MTYxNDU4NzEzODA4OQ.GOpqYr.bRD6De03Z-gTKVacmys44NTgoi4ZgvR5UP789U')