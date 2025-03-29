# Source: https://discordpy.readthedocs.io/en/stable/quickstart.html

# How to run:
# 1) In terminal, add `DISCORD_TOKEN` environment variable to store bot's token
# 2) In terminal, run `python main.py` to start the bot

import settings
import discord
from discord.ext import commands
from summarise import get_summary, fetch_recent_messages

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info(f"Guild ID: {bot.guilds[0].id}")
        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)

    @bot.tree.command(description="Summarise messages from the last 7 days")
    async def summarise(interaction: discord.Interaction):
        await interaction.response.defer() # Acknowledge the interaction immediately.
        try:
            channel = interaction.channel
            messages = await fetch_recent_messages(channel)

            if not messages:
                await interaction.followup.send("No messages found in the last 7 days.")
                return
            
            summary = get_summary(messages)
            await interaction.followup.send(f"📋 Summary:\n{summary}")
        except Exception as e:
            await interaction.followup.send(f"⚠️ Error: {str(e)}")

    bot.run(settings.DISCORD_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()