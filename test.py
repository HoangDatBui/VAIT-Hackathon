from llama_index.readers.discord import DiscordReader
from llama_index.core import SummaryIndex
import os

# Set your Discord token
os.environ["DISCORD_TOKEN"] = os.getenv("DISCORD_TOKEN")

# Load data from a Discord channel
discord_reader = DiscordReader()
channel_ids = [1355381192035405967]  # Replace with your actual channel ID

# Fetch messages as documents
documents = discord_reader.load_data(channel_ids=channel_ids)

# Save messages into a text file
with open("discord_channel_messages.txt", "w", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc.text.strip() + "\n")

# Create a SummaryIndex from the loaded documents
# index = SummaryIndex.from_documents(documents)

# # Query the index to get a summary
# summary = index.query("Summarize the chatlog")
# print(summary)