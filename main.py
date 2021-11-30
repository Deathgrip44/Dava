#Importing Libraries

from typing import Text
import speech_recognition as sr

r = sr.Recognizer()

#Gets default microphone
with sr.Microphone() as source:
    # Listens to a command with AVD
    audio = r.listen(source)

    Text = r.recognize_google(audio)

    print(Text)