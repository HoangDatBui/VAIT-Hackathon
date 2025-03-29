import settings
import os
from openai import OpenAI

def get_summary():

    # Initialize DeepSeek client
    client = OpenAI(api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

    # Hardcoded messages for testing
    messages = [
        "Hey, I'm trying to get into DevOps. Any suggestions on where to start?",
        "Yeah, start with understanding basic Linux and networking.",
        "Cloud is a must—maybe start with AWS or Azure fundamentals.",
        "Don't forget to learn Git and version control.",
        "For Infrastructure as Code, Terraform is super popular.",
        "Also, CI/CD tools like Jenkins or GitHub Actions are essential.",
        "Kubernetes is useful if you want to go deeper into orchestration.",
    ]

    # Build the prompt
    chat_messages = [
        {"role": "system", "content": "Summarize the following conversation briefly."},
        {"role": "user", "content": "\n".join(messages)}
    ]

    # Call the DeepSeek API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=chat_messages,
        stream=False
    )

    return response.choices[0].message.content.strip()