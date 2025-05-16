import os
import google.generativeai as genai
from dotenv import load_dotenv
from voice import speak

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Debug check
print("🔑 Loaded Gemini Key:", api_key[:8] + "..." if api_key else "❌ Not loaded")

# Configure SDK
genai.configure(api_key=api_key)

# Ask Gemini Function (Chat-based version)
def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        convo = model.start_chat(history=[])
        convo.send_message(prompt)
        reply = convo.last.text
        speak(reply)
        return reply
    except Exception as e:
        speak("Sorry, I ran into an error with Gemini.")
        print("❌ Gemini Error:", e)
        return ""
