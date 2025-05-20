from flask import Flask, request, jsonify
from commands import greet, tell_time, open_website, search_google, open_app
from llm_gemini import ask_gemini, load_gemini
from voice import speak
import threading
from flask_cors import CORS  # ✅ Add this

app = Flask(__name__)
CORS(app)  # ✅ Allow frontend requests

# Launch Gemini preload
threading.Thread(target=load_gemini).start()

@app.route("/api/ask", methods=["POST"])
def handle_input():
    user_input = request.json.get("prompt", "").lower()
    
    response = ""
    if "time" in user_input:
        response = tell_time()
    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        response = search_google(query)
    elif "open" in user_input:
        site_or_app = user_input.replace("open", "").strip()
        if "." in site_or_app or site_or_app in ["youtube", "gmail", "google"]:
            response = open_website(site_or_app)
        else:
            response = open_app(site_or_app)
    elif "exit" in user_input or "quit" in user_input:
        response = "Goodbye!"
    else:
        response = ask_gemini(user_input)

    speak(response)  # Optional: Text-to-speech

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
