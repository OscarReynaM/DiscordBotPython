import discord
import youtube_dl
import os
from os import system
from discord.ext import commands
from discord.ext.commands import Bot
from discord import FFmpegPCMAudio
from discord.utils import get
import random

client = commands.Bot(command_prefix='=')
#client = discord.Client()
counter = 0
total = 0
id = 000000000000000000


@client.event
async def on_ready():
    print('Logged on as', client.user)

@client.event
async def on_disconnect(self):
    print ("Aiko going offline.")
    
@client.command(aliases=['f', 'F'])
async def _f(ctx):
    global total
    total = total + 1
    embed = discord.Embed(description = f'{ctx.author.mention} has paid their respects.')
    embed.set_footer(text= ' Total: ' + str(total))
    
    await ctx.send(embed=embed)    


#Codigo para unirse al canal y poner musica, sigue en desarrollo

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    if not channel:
        await ctx.send('No estas en un VC :p')
        return
    
    await channel.connect()
    
@client.command(pass_context=True, brief="This will play a song 'play [url]'", aliases=['p'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Espera a que termine el rolon")
        return
    
    await ctx.send("Preparando rolon, dame unos segundos")
    print("Alguien puso un rolon, deja lo pongo.....")
    
    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'default_search': 'auto',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()



@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    

@client.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == client.user:
        return

    if message.content == 'ping':
        await message.channel.send('pong')
    
    if (message.author.id == 324383693248659456):
        valor = random.randint(0,10)
        
        if (valor == 0):
            size = message.content
            output = ""
            for i in range(len(size)):
                for letter in size[i].lower():
                    if (random.randint(0,100))% 2 == 0:   
                        output += letter.lower()
                    else:
                        output += letter.upper()
            
            await message.channel.send(output)
            
        if (valor == 1):
            await message.channel.send('Eres el mejor')
            
        if (valor == 2):
            await message.channel.send('Mejor ponte a traducir')
            
        if (valor == 3):
            await message.channel.send('Donde esta la novela?')
            
        if (valor == 4):
            await message.channel.send('Ya desayunaste?')
            
        if (valor == 5):
            await message.channel.send('Hola Ray, nomas queria tomarme este minuto para decir que te quiero, eres una gran persona, si estas pasando por un mal momento en tu vida sabe que tienes amigos con quien platicar y se tomarian el tiempo para escucharte. Nos sentimos bendecidos porque te tenemos alrededor de nosotros y esperamos que sigas ahi. Hemos pasado por muchos momentos de risa y estamos agradecidos por ello. Eres la persona que se puede contar para tener unas buenas risas.')
        
    
    #Codigo para el texto de Mucho Texto
    global id
    global counter
                        
    if (message.author.id == id):
        counter += 1
    else:
        counter = 1
    
    if (counter >= 15):
        await message.channel.send('Mucho Texto')
        counter = 1
        
    id = message.author.id
    
    await client.process_commands(message)
    
    
    
    #-----------------------------------------------
            

client.run('NzIwMjc2MzMzNzgyODkyNjM2.XuDnnA.LVhJ0Gp7e2OUp1RZQs7U8Ankzoc')

#Id de ray  324383693248659456
#Id de jesusu  166675689506996234
#Id de paco  210469827972694016
#Id de Oscar  129103410912952320
#Id de Mau  289032318482382848
