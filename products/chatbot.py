import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY", "")


def get_response(user_input):
    if not API_KEY:
        return "Gemini API key is not configured. Please set GEMINI_API_KEY in your .env file."

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": user_input}]
        }]
    }

    try:
        response = requests.post(url, json=payload).json()
        print("Response from Gemini:")
        print(response)

        if "candidates" not in response:
            return str(response)

        return response["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error connecting to Gemini API: {str(e)}"