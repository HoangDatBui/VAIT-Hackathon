# Source: https://discordpy.readthedocs.io/en/stable/quickstart.html

# How to run:
# 1) In terminal, add `DISCORD_TOKEN` environment variable to store bot's token
# 2) In terminal, run `python main.py` to start the bot
# 3) In server, send `$hello` message to see the bot respond

import os
import discord
from summarise import get_summary

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("test summarise"):
        await message.channel.send("Working on your summary...")

        try:
            summary = get_summary()
            await message.channel.send(f"📋 Summary:\n{summary}")
        except Exception as e:
            await message.channel.send(f"⚠️ Error: {str(e)}")


token = os.getenv("DISCORD_TOKEN")
if token is None:
    raise ValueError("DISCORD_TOKEN is not set")

client.run(token)