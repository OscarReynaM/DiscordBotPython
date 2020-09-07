import discord
from discord.ext import commands

hoy = 0
total = 0

bot = commands.Bot(command_prefix='$')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            
        if message.content == 'mau':
            await message.channel.send('es gey')
     
    @bot.command()       
    async def test(ctx):
        await ctx.send('comic sans')

client = MyClient()
client.run('NzIwMjc2MzMzNzgyODkyNjM2.XuEUow.2N3TGkb_mP4VCiFRUhv4VNmHBks')


"""
embed=discord.Embed(title=@user has paid their respects, color=0xc517e8)
embed.set_footer(text=# Today, # All)
await self.bot.say(embed=embed)
"""