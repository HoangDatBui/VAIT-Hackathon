import logging
import discord
import settings

from discord.ext import commands
from summarise import get_summary, Channel

logger = logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info(f"Guild IDs: {[guild.id for guild in bot.guilds]}")

    @bot.tree.command(description="Summarise messages from the last 7 days")
    async def summarise(interaction: discord.Interaction):
        await interaction.response.defer()  # Acknowledge the interaction immediately.

        try:
            if interaction.channel is None:
                raise ValueError("Channel not found")
            if not isinstance(interaction.channel, Channel):
                raise ValueError("Channel is not a text channel or thread")
            summary = await get_summary(interaction.channel)
            await interaction.followup.send(f"📋 Summary:\n{summary}")
            logger.info(
                f"Summarised {interaction.channel.name} ({interaction.channel.id}) in {interaction.guild.name} ({interaction.guild.id})"
            )

        except Exception as e:
            await interaction.followup.send(f"⚠️ Error: {str(e)}")

    bot.run(settings.DISCORD_TOKEN, root_logger=True)


if __name__ == "__main__":
    run()
