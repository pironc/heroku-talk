import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

channel = client.get_channel(938925751904899125)

@client.command()
async def hello(ctx):
	await ctx.channel.send("world")

client.run("OTM4OTI3MzEzNTgyNjk4NDk2.YfxaMw.mKH8IQ8T-SuOOS1IwbrK8Y7-eoA")