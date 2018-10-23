import discord

from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

TOKEN = 'NTA0NDI3MTcwNTc2NDY1OTIw.DrE4GA.pwYbqEn58AwgQsKHWoqtHTgO8lc'

client = Bot(command_prefix="--")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)


@client.event
async def on_ready():
    print ("Fake Ben is ready")
    print ("Running on bot user name: " + client.user.name)
    print ("With bot userID: " + client.user.id)


@client.command()
async def echo(*args):
    print("echo() just ran")
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)



try:
    with open("./cogs/command.py") as file:
        pass
except IOError:
    print("The file could not be opened.")

#Runs the bot user with the right token (one from line 8)       
client.run(TOKEN)
