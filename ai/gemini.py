import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(prompt):
    """
    Send user prompt to Gemini and return the response.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""
You are DORA, an intelligent desktop AI assistant.

Rules:
- Keep spoken responses concise (2-4 sentences).
- Be friendly.
- If the user asks for a long explanation, provide it.

User:
{prompt}
"""
        )

        return response.text

    except Exception as e:
        return f"Sorry Devansh, I encountered an error.\n{e}"