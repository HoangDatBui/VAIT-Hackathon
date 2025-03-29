# Source: https://discordpy.readthedocs.io/en/stable/quickstart.html

# How to run:
# 1) In terminal, dd `DISCORD_TOKEN` environment variable to store bot's token
# 2) In terminal, run `python main.py` to start the bot
# 3) In server, send `$hello` message to see the bot respond

import os
import discord

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

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


token = os.getenv("DISCORD_TOKEN")
if token is None:
    raise ValueError("DISCORD_TOKEN is not set")

client.run(token)
