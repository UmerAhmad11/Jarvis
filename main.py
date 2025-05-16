from voice import listen, speak
from commands import greet, tell_time, open_website, search_google, open_app
from llm_gemini import ask_gemini
import time
import sys
import threading
from llm_gemini import load_gemini

# Launch Gemini preload in parallel
threading.Thread(target=load_gemini).start()

def thinking_timer():
    print("")  # Newline for clean console output
    start = time.time()
    while True:
        elapsed = time.time() - start
        sys.stdout.write(f"\r🤖 Thinking... {elapsed:.1f} seconds")
        sys.stdout.flush()
        time.sleep(0.1)
        if stop_timer:
            break
    print("\n")

# Global flag
stop_timer = False

def start_thinking():
    global stop_timer
    stop_timer = False
    threading.Thread(target=thinking_timer).start()
    

def main():
    greet()
    while True:
        user_input = listen()
        if "time" in user_input:
            tell_time()
        elif "search" in user_input:
            search_google(user_input.replace("search", "").strip())
        elif "open" in user_input:
            site_or_app = user_input.replace("open", "").strip()
            if "." in site_or_app or site_or_app in ["youtube", "gmail", "google"]:
                open_website(site_or_app)
            else:
                open_app(site_or_app)
        elif "exit" in user_input or "quit" in user_input:
            speak("Goodbye!")
            break
        # Inside the main loop:

        else:
            ask_gemini(user_input)
            stop_timer = True

if __name__ == "__main__":
    main()
