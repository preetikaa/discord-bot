import discord
from discord.ext import commands
TOKEN=

client=commands.Bot(command_prefix=".")

@client.command()
async def hello(ctx):
    s="Hello World"
    await ctx.send(s)


client.run(TOKEN)
