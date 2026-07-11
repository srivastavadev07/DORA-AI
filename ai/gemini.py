import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def ask_gemini(prompt):
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "system",
                    "content": """You are DORA, an intelligent desktop AI assistant.

Keep responses short unless the user requests details.
Be friendly.
""",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Sorry Devansh, I encountered an error.\n{e}"