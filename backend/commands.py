import webbrowser
import datetime
import os
from voice import speak

def greet():
    response = "Hello! How can I help you today?"
    speak(response)
    return response

def tell_time():
    now = datetime.datetime.now().strftime("%H:%M")
    response = f"The time is {now}"
    speak(response)
    return response

def open_website(site):
    sites = {
        "youtube": "https://youtube.com",
        "gmail": "https://mail.google.com",
        "google": "https://google.com"
    }
    url = sites.get(site.lower(), f"https://{site}.com")
    response = f"Opening {site}"
    speak(response)
    webbrowser.open(url)
    return response

def search_google(query):
    response = f"Here are the search results for {query}"
    speak(response)
    webbrowser.open("https://google.com/search?q=" + query)
    return response

def open_app(name):
    response = f"Opening {name}"
    speak(response)
    if os.name == 'nt':  # Windows
        os.system(f'start {name}')
    else:  # macOS/Linux
        os.system(f'open -a "{name}"')
    return response
