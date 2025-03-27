import pyttsx3
import threading

def speak(text):
    def run_tts():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    tts_thread = threading.Thread(target=run_tts)
    tts_thread.start()
