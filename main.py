import settings
import discord
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        await bot.tree.sync()

    @bot.hybrid_command()
    async def troll(ctx):
        await ctx.send("sos tremendo trolazo")

    @bot.command()
    async def mensaje(ctx, mensaje):
        await ctx.send(mensaje)



    bot.run(settings.TOKEN)
if __name__ == "__main__":
    run()