import speech_recognition as sr
import pyttsx3
import threading
import queue
import time

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Create a queue for speech
speech_queue = queue.Queue()
stop_speaking = threading.Event()

# TTS worker thread
def tts_worker():
    while not stop_speaking.is_set():
        try:
            text = speech_queue.get(timeout=0.1)
            print("Jarvis:", text)
            engine.say(text)
            engine.runAndWait()
            speech_queue.task_done()
        except queue.Empty:
            continue
        except Exception as e:
            print("⚠️ TTS error:", e)

# Start the TTS thread
tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def speak(text):
    speech_queue.put(text)

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
