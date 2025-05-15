import google.generativeai as genai
import os
from dotenv import load_dotenv
from voice import speak

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = model.generate_content(prompt)
        reply = response.text
        speak(reply)
        return reply
    except Exception as e:
        speak("Sorry, I ran into an error with Gemini.")
        print("Gemini Error:", e)
        return ""
