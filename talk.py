import discord
from discord.ext import commands
import requests
import os

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

channel = client.get_channel(938925751904899125)

@client.command()
async def hello(ctx):
	await ctx.channel.send("world")

client.run(os.environ.get("TOKEN"))