from gtts import gTTS
import time

text = input("Enter text here: ")
filename = input("Enter filename here: ")
tts = gTTS(text, lang="en")
tts.save(f"C:/Users/ryana/Downloads/{filename}.mp3")
print("Saved in downloads folder")
time.sleep(0.5)
