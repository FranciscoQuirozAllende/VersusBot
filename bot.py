import os

import discord

from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}\n')

    for guild in client.guilds:
        print(f'conectado a ' + guild.name +'\n')

client.run(TOKEN)