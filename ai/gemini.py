import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt):
    """
    Send user prompt to Gemini and return the response.
    """

    try:
        response = model.generate_content(
    f"""
    You are DORA, an intelligent desktop AI assistant.

    Keep spoken responses concise (2-4 sentences) unless the user explicitly asks for a detailed explanation.

    User: {prompt}
    """
)

        return response.text

    except Exception as e:
        return f"Sorry Devansh, I encountered an error.\n{e}"