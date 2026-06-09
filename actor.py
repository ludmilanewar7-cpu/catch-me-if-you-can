import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def run_actor(task, style, message, conversation_history=""):
    if conversation_history:
        prompt = f"""You are an AI assistant helping a user with a task.

Your task is: {task}

Your communication style: {style}

Here is the conversation history so far:
{conversation_history}

User message: {message}"""
    elif style:
        prompt = f"""You are an AI assistant helping a user with a task.

Your task is: {task}

Your communication style: {style}

User message: {message}"""
    else:
        prompt = f"""You are an AI assistant helping a user with a task.

Your task is: {task}

User message: {message}"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
