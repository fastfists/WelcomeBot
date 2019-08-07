import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

j_index = 0
jasons = ["jason", "JASON", "JASON!", "JASON?"]

bot = commands.Bot(command_prefix='!')

"""Event handler
"""
@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.event
async def on_message(message):
    global j_index, jasons
    tokens = message.content.upper().split(' ')
    print(tokens)
    if "X" in tokens:
        await bot.send_message(message.channel, jasons[j_index])
        j_index = (j_index + 1) % 4
    if "F" in tokens:
        await bot.send_message(message.channel, "Respects have been paid")

bot.run("445793039479341057")
