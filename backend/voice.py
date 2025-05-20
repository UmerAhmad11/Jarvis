import speech_recognition as sr
import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 150)

tts_lock = threading.Lock()

def _speak_worker(text):
    with tts_lock:
        try:
            print("Jarvis:", text)
            engine.say(text)
            engine.runAndWait()
        except RuntimeError:
            print("⚠️ TTS engine is already speaking. Ignored.")

def speak(text):
    threading.Thread(target=_speak_worker, args=(text,), daemon=True).start()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""
