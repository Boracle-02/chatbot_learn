import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os

# chatbot obj
class ChatBot():
    def __init__(self, name):
        print("Chatbot", name, "has started up.")
        self.name = name

    # have chatbot turn user speech into text for analysis using google's api
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("You said:", self.text)
        except:
            # do nothing when bot hears nothing
            print("error")
    
    # let the chatbot say smth back
    # since we want to be able to call this without having a chatbot obj
    @staticmethod
    def text_to_speech(text):
        print("I will say", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3") 
        os.remove("res.mp3")

    # have the chatbot sleeping then when it detects its name, wake up
    def wake_up(self, text):
        if self.name in text.lower():
            return True
        return False

    
if __name__ == "__main__":
    ai = ChatBot("test")
    while True:
         ai.speech_to_text()
         if ai.wake_up(ai.text) is True:
            res = "Hello I am a test chatbot, what can I do for you?"
            ai.text_to_speech(res)
