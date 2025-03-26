import pyttsx3

#This should convert text to speach ***cross my fingers***#

# Initialize the engine globally (outside function) i am trying to prevent repetition in speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def speak(words):
    engine.stop()  # Stop any ongoing speech before speaking new words
    engine.say(words)
    engine.runAndWait()
