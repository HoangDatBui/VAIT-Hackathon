# Source: https://discordpy.readthedocs.io/en/stable/quickstart.html

# How to run:
# 1) In terminal, add `DISCORD_TOKEN` environment variable to store bot's token
# 2) In terminal, run `python main.py` to start the bot
# 3) In server, send `$hello` message to see the bot respond

import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

bot.run(settings.DISCORD_TOKEN, root_logger=True)