import pyttsx3

#This should convert text to speach ***cross my fingers***#

# Initialize the engine globally (outside function) i am trying to prevent repetition in speech
engine = pyttsx3.init()

def speak(words):
    engine.stop()  # Stop any ongoing speech before speaking new words
    engine.say(words)
    engine.runAndWait()
