import discord
from discord.ext import commands

client = commands.Bot(command_prefix='=')

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def f(ctx):
    #await ctx.send(f'{ctx.author.mention} has paid their respects', colour = discord.Colour.purple())
    embed = discord.Embed(description = f'{ctx.author.mention} has paid their respects.')
    embed.set_footer(text= ' Today, Total')
    await ctx.send(embed=embed)
    
    

client.run('NzIwMjc2MzMzNzgyODkyNjM2.XuEUow.2N3TGkb_mP4VCiFRUhv4VNmHBks')
