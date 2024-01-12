import settings
import discord
import random
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        await bot.tree.sync()#se sincronizan los comandos del bot

    #comando para spamear el mensaje spam
    #para multiplicar str y que no de problemas hay que definir el tipo de la variable
    #usar con conocimiento de causa
    @bot.hybrid_command()
    async def spam(ctx, cantidad: int):
        var = ("@everyone\n")
        i = 1
        if cantidad == 0:
            await ctx.send("aweonao ql como se te ocurre poner eso xDDDDD")
        else:
            while i <= cantidad:
                await ctx.send(var)
                i += 1

    @bot.hybrid_command()
    async def versus(ctx, tamaño_equipo: int, jugadores):
        lista_jugadores = jugadores.split(',')
        equipo1= []
        equipo2= []
        
        while 1 <= len(lista_jugadores):
            ran = random.choice(lista_jugadores)
            if ran not in equipo1 and len(equipo1) < tamaño_equipo:
                equipo1.append(ran)
            else:
                equipo2.append(ran)
            lista_jugadores.remove(ran)

        respuesta = "Equipo 1: " + ' '.join(equipo1)  + "\nEquipo 2: " + ' '.join(equipo2)
        await ctx.send(respuesta)

    #este comando es el que inicializa el botd
    #tiene que ir al final para que se carge todo lo que esta antes
    #soy terrible weon para poner comentarios xDDDD
    bot.run(settings.TOKEN)

if __name__ == "__main__":
    run()