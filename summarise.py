import settings
import os
from openai import OpenAI
import discord
from datetime import datetime, timedelta

async def get_summary(channel: discord.channel):
    messages = await fetch_recent_messages(channel)

    if not messages:
        return "No messages found"
    return fetch_response(messages)

async def fetch_recent_messages(channel, days=7):

    # Calculate the date from 7 days ago
    one_week_ago = datetime.now() - timedelta(days=days)

    messages = []
    async for msg in channel.history(limit=None, after=one_week_ago):
        # Skip messages from bots and empty messages
        if not msg.author.bot and msg.content.strip():
            messages.append(f"{msg.author.display_name}: {msg.content}")

    return messages

def fetch_response(message_list=None):
    # Initialize DeepSeek client
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com"
    )

    # Build the prompt
    chat_messages = [
        {"role": "system", "content": "Summarise the following conversation briefly."},
        {"role": "user", "content": "\n".join(message_list)},
    ]

    # Call the DeepSeek API
    response = client.chat.completions.create(
        model="deepseek-chat", messages=chat_messages, stream=False
    )

    return response.choices[0].message.content.strip()
