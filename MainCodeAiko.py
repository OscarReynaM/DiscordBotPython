import discord
from discord.ext import commands
import random

client = discord.Client()
counter = 0
id = 000000000000000000

#client = commands.Bot(command_prefix='=')

@client.event
async def on_ready():
    print('Logged on as', client.user)
    

@client.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == client.user:
        return

    if message.content == 'ping':
        await message.channel.send('pong')
        
    if (message.content == 'F' or message.content == 'f' or message.content == '=F' or message.content == '=f'):
        myembed = discord.Embed(description = f'{message.author.mention} has paid their respects.')
        await message.channel.send(embed=myembed)
    
    if (message.author.id == 324383693248659456):
        valor = random.randint(0,7)
        
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
            await message.channel.send('Ya callate we')
            
        if (valor == 2):
            await message.channel.send('Que es puto dicen')
            
        if (valor == 3):
            await message.channel.send('Mejor ponte a traducir')
            
        if (valor == 4):
            await message.channel.send('Donde esta la novela?')
            
        if (valor == 5):
            await message.channel.send('Mejor come un pene')
            
        if (valor == 6):
            await message.channel.send('Ya deja de ser negro')
            
        if (valor == 7):
            await message.channel.send('Hola Ray, nomas queria tomarme este minuto para decir que te quiero, eres una gran persona, si estas pasando por un mal momento en tu vida sabe que tienes amigos con quien platicar y se tomarian el tiempo para escucharte. Nos sentimos bendecidos porque te tenemos alrededor de nosotros y esperamos que sigas ahi. Hemos pasado por muchos momentos de risa y estamos agradecidos por ello. Eres la persona que se puede contar para tener unas buenas risas. Tambien vales verga.')
            
@client.event
async def on_message(message): #funcion para devolver mucho texto a una persona despues de 15 mensajes
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

            
    
    

client.run('NzIwMjc2MzMzNzgyODkyNjM2.XuDnnA.cBKj3PzfhKatqabsZwooW69qhyk')

#Id de ray  324383693248659456
#Id de jesusu  166675689506996234
#Id de paco  210469827972694016
#Id de Oscar  129103410912952320
#Id de Mau  289032318482382848
