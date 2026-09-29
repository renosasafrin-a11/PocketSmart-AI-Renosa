import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY) if API_KEY else None


async def generate_recommendation(prompt: str):
    """
    Generate a recommendation using Gemini.
    """

    if client is None:
        return "Gemini API key is not configured."

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini API error: {str(e)}"