import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import datetime
# pip install playsound==1.2.2
from playsound import playsound
import time

# chatbot obj
class ChatBot():
    def __init__(self, name):
        print("Chatbot", name, "has started up.")
        self.name = name
        self.user_input = ""
        self.speak = True

    def get_input(self):
        self.user_input = input("What would you like to say to me?\n")

    # let the chatbot say smth back
    # since we want to be able to call this without having a chatbot obj
    @staticmethod
    def text_to_speech(text):
        print("I will say", text)
        speaker = gTTS(text=text, lang="en", slow=False)

        # program may be trying to save/ in progress of saving while playsound is called
        # add to remove any previous
        # file = os.path.join(os.getcwd(), "audio.mp3")
        speaker.save("audio.mp3")

        playsound("audio.mp3")

        os.remove("audio.mp3")


    # have the chatbot sleeping then when it detects its name, wake up
    def wake_up(self, text):
        if self.name in text.lower():
            return True
        return False

    # get the time in army time 
    @staticmethod
    def get_time():
        # %H gets hour remember from clock %I is 1-12
        return datetime.now().time().strftime('%H:%M')
    
if __name__ == "__main__":
    chatty = ChatBot("test")
    # chatty.speak = True if input("Enter Y if you would like me to talk to you.\n").startswith("Y")
    ask_user_speak = input("Enter Y if you would like me to talk to you.\n")
    chatty.speak = True if ask_user_speak.startswith("Y") or ask_user_speak.startswith("y") else False
    
    chatty.get_input()
    while chatty.user_input != "exit":
        res = ""
        
        if chatty.wake_up(chatty.user_input):
            res = "Hello I am a test chatbot, what can I do for you?"
            
        elif "time" in chatty.user_input:
            res = chatty.get_time()
        
        try:
            if chatty.speak:
                print(res)
                chatty.text_to_speech(res)
            else:
                # since the print occurs after the text finishes talking, i will have it print first then talk
                print(res)
        except:
            # try to say smth if there is nothing to say, error will occur
            print("I did not quie catch that")

        chatty.get_input()
