import webbrowser
import datetime
import os
from voice import speak

def greet():
    speak("Hello! How can I help you today?")

def tell_time():
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {now}")

def open_website(site):
    sites = {
        "youtube": "https://youtube.com",
        "gmail": "https://mail.google.com",
        "google": "https://google.com"
    }
    url = sites.get(site, f"https://{site}.com")
    speak(f"Opening {site}")
    webbrowser.open(url)

def search_google(query):
    speak(f"Here are the search results for {query}")
    webbrowser.open("https://google.com/search?q=" + query)

def open_app(name):
    if os.name == 'nt':  # Windows
        os.system(f'start {name}')
    else:  # macOS/Linux
        os.system(f'open -a "{name}"')
