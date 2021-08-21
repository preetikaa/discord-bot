import discord
from discord.ext import commands

TOKEN = ""
client = commands.Bot(command_prefix=".")

@client.command()
async def hello(ctx):
    s = f"Hello {ctx.author.mention}, have a good day!"
    await ctx.send(s)
    
client.run(TOKEN)
