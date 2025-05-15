from voice import listen, speak
from commands import greet, tell_time, open_website, search_google, open_app

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

if __name__ == "__main__":
    main()
