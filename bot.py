import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '!' )
# !help
  
@client.event

async def on_ready():
    print('Bot in online')

@client.command (pass_context = True)

async def салам( ctx ):
    author = ctx.message.author

    await ctx.send(f'{ author.mention } салам брат')

@client.command (pass_context = True)

async def поменяйдиски( ctx ):
    author = ctx.message.author

    await ctx.send(f'{author.mention} соси хуй брат')
@client.command (pass_context = True)

async def info( ctx ):
    author = ctx.message.author

    await ctx.send(f'{author.mention} **Приветствую тебя на данном дискорд сервере.** Здесь мы тупо общаемся и гамаем в игры')

# connect
client.run('NzEwNDEyNjMwNzE5NzI1NTk4.XtlEag.7ScVqe5vZvf0vz3ofD8XYyDS_SA')
