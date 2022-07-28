from gtts import gTTS 
import os
from playsound import playsound
speak= input("Enter Anything ")
file = open("abc.txt", "w").write(speak)
file = open("abc.txt", "r").read()

speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")
# os.system("mv voice.mp3 voice.mp3")
playsound("voice.mp3")

# print(file)
