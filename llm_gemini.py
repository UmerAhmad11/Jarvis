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

def load_gemini():
    global convo
    # ✅ Preload model and chat session
    try:
        print("⚙️ Initializing Gemini chat session in background...")
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        convo = model.start_chat(history=[])
        try:
            convo.send_message("Hello")
            if convo.last.text:
                print("✅ Gemini chat session is ready!")
        except Exception as e:
            print("Error Getting Reply: ", e)
    except Exception as e:
        print("❌ Error initializing Gemini:", e)
        

# Ask Gemini Function (Chat-based version)
def ask_gemini(prompt):
    global convo
    if convo is None:
        speak("Gemini is not initialized yet.")
        print("❌ Gemini session not initialized. Call load_gemini() first.")
        return ""

    prompt = prompt.strip()
    if not prompt:
        print("⚠️ Empty prompt received. Skipping Gemini call.")
        return ""

    try:
        print("🤖 Thinking...", end=" ", flush=True)
        import time
        start_time = time.time()
        convo.send_message(prompt)
        reply = convo.last.text
        elapsed = round(time.time() - start_time, 1)
        print(f"{elapsed} seconds")
        print("Jarvis:", reply)
        speak(reply)
        return reply
    except Exception as e:
        speak("Sorry, I ran into an error with Gemini.")
        print("❌ Gemini Error:", e)
        return ""

