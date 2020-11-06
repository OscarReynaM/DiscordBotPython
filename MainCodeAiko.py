import discord
from discord.ext import commands
import random

client = discord.Client()
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
        size = message.content
        output = ""
        for i in range(len(size)):
            for letter in size[i].lower():
                if (random.randint(0,100))% 2 == 0:   
                    output += letter.lower()
                else:
                    output += letter.upper()
        
        await message.channel.send(output)
    

client.run('NzIwMjc2MzMzNzgyODkyNjM2.XuDnnA.cBKj3PzfhKatqabsZwooW69qhyk')

#Id de ray324383693248659456
# Id de jesusu 166675689506996234
#id de paco 210469827972694016
