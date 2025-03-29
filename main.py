# Source: https://discordpy.readthedocs.io/en/stable/quickstart.html

# How to run:
# 1) In terminal, add `DISCORD_TOKEN` environment variable to store bot's token
# 2) In terminal, run `python main.py` to start the bot
# 3) In server, send `$hello` message to see the bot respond

import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info(f"Guild ID: {bot.guilds[1].id}")
        bot.tree.copy_global_to(guild=settings.GUILD_ID)
        await bot.tree.sync(guild=settings.GUILD_ID)

    @bot.tree.command(description="Summarise messages")
    async def summarise(interaction: discord.Interaction):

        #TODO
        await interaction.response.send_message(f"Summarising for user {interaction.user.mention}", ephemeral=True)

    bot.run(settings.DISCORD_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()