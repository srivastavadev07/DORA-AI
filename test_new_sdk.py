import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

print("API Key Loaded:", os.getenv("GEMINI_API_KEY")[:15] + "...")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Say Hello."
    )

    print(response.text)

except Exception as e:
    print(type(e))
    print(e)