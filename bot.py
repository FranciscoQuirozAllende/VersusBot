import os

import discord

from dotenv import load_dotenv

from discord.ext import commands

#se cargan los permisos del bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#se carga el token desde el archivo .env
load_dotenv()
TOKEN = os.getenv('TOKEN')

#se establece el comando para ejecutar el bot con los respectivos permisos
bot = commands.Bot(command_prefix='!', intents=intents, description='puras weas')

@bot.command()
async def mensaje(ctx, mensaje):
    await ctx.send(mensaje)

bot.run(TOKEN)