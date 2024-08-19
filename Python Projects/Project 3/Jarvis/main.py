import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from gtts import gTTS
import pygame
import os
import wikipedia
import sys

# Initialize speech recognition and text-to-speech
recog = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak using pyttsx3
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# Function to speak using gTTS and pygame
def speak(text):
    tts = gTTS(text)
    tts.save('text.mp3')

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the MP3 file
    pygame.mixer.music.load("text.mp3")
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("text.mp3")

# Function to process command using OpenAI GPT-3.5
def aiProcess(command):
    print("Searching on Wikipedia... Please wait.")
    speak("Searching on Wikipedia... Please wait.")
    summary = wikipedia.summary(command, sentences=2)
    print("According to Wikipedia:\n")
    speak("According to Wikipedia:\n")
    print(summary)
    speak(summary)

# Function to handle the recognized command
def processCommand(c):
    c_lower = c.lower()
    api_Key = os.getenv("NEWS_API_KEY")

    if "open" in c_lower:
        website = c_lower[5:].strip()

        if website:
            webbrowser.open(f"http://{website}.com")
        else:
            speak("Please specify a website to open.")

    elif "play" in c_lower:
        music = c_lower[5:].strip()
        if music:
            webbrowser.open(f"https://www.youtube.com/results?search_query={music}")

    elif "news of" in c_lower:
        news = c_lower[8:].strip()
        data = requests.get(f"https://newsapi.org/v2/top-headlines?country={news}&apiKey={api_Key}")
        if data.status_code == 200:
            x = data.json()
            articles = x.get('articles', [])
            for i in articles:
                title = i['title']
                print(title)
                speak(title)
        else:
            speak("Failed to fetch news.")

    elif "vs code" in c_lower:
        codePath = "C:\\Users\\madrassa v145\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif "exit" in c_lower or "quit" in c_lower:
        speak("Goodbye!")
        sys.exit()

    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recog.listen(source, timeout=3, phrase_time_limit=2)
                word = recog.recognize_google(audio).lower()

            if word == "jarvis":
                speak("Yes?")
                print("Jarvis Activated...")

                with sr.Microphone() as source:
                    audio = recog.listen(source, timeout=5, phrase_time_limit=3)
                    command = recog.recognize_google(audio).lower()

                processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))