from typing import Union
import discord
from openai import OpenAI
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from datetime import datetime, timedelta

import settings

Channel = Union[
    discord.channel.TextChannel,
    discord.threads.Thread,
]


async def get_summary(channel: Channel) -> str:
    messages = await fetch_recent_messages(channel)

    if not messages:
        return "No messages found"
    return fetch_response(messages)


async def fetch_recent_messages(channel: Channel, days: int = 7) -> list[str]:
    # Calculate the date from 7 days ago
    one_week_ago = datetime.now() - timedelta(days=days)

    messages = []
    async for msg in channel.history(limit=None, after=one_week_ago):
        # Skip messages from bots and empty messages
        if not msg.author.bot and msg.content.strip():
            messages.append(f"{msg.author.display_name}: {msg.content}")

    return messages


def fetch_response(message_list: list[str]) -> str:
    # Initialize DeepSeek client
    client = OpenAI(
        api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com"
    )

    # Build the prompt
    chat_messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": "Summarise the following conversation briefly."},
        {"role": "user", "content": "\n".join(message_list)},
    ]

    # Call the DeepSeek API
    response = client.chat.completions.create(
        model="deepseek-chat", messages=chat_messages, stream=False
    )
    if not response.choices[0].message.content:
        raise Exception("No response from DeepSeek API")

    return response.choices[0].message.content.strip()
