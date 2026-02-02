import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pywhatkit
import pyautogui
import psutil
import os
import random
from googletrans import Translator
import time


engine = pyttsx3.init()
engine.setProperty('rate', 150)
r = sr.Recognizer()
translator = Translator()

def speak(text):
    print('Assistant:', text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # ensures next speech starts fresh


def listen(timeout=6, phrase_time_limit=6):
    try:
        with sr.Microphone() as source:
            print('Listening...')
            r.adjust_for_ambient_noise(source, duration=0.6)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        text = r.recognize_google(audio, language='en-in')
        print('You:', text)
        return text.lower()

    except sr.WaitTimeoutError:
        print("Listening timeout — no voice detected.")
        return ''

    except:
        return ''


def get_time():
    return datetime.datetime.now().strftime('%H:%M')

def search_wikipedia(query, sentences=2):
    try:
        return wikipedia.summary(query, sentences=sentences)
    except:
        return "Sorry, I couldn’t find that on Wikipedia."

def main():
    speak('Hello Pavan — I am your upgraded assistant. Say a command.')
    time.sleep(0.5)


    while True:
        text = listen()
        if not text:
            speak('Please repeat your command.')
            continue

        if 'time' in text:
            speak('The time is ' + get_time())
            time.sleep(0.3)

        elif 'open youtube' in text:
            webbrowser.open('https://youtube.com')
            speak('Opening YouTube')
            time.sleep(0.3)


        elif 'open instagram' in text:
            speak('Opening Instagram')
            time.sleep(0.3)
            webbrowser.open('https://instagram.com')
           


        elif 'open whatsapp' in text:
            speak('Opening WhatsApp Web')
            time.sleep(0.3)
            webbrowser.open('https://web.whatsapp.com')
           
            


        elif 'play song' in text or 'play music' in text:
            speak('Which song should I play?')
            song = listen()
            time.sleep(0.3)
            pywhatkit.playonyt(song)
            speak(f'Playing {song} on YouTube')
            time.sleep(0.3)

        elif 'battery' in text:
            battery = psutil.sensors_battery()
            if battery:
                speak(f'Battery is at {battery.percent} percent.')
            else:
                speak('Sorry, I cannot detect a battery on this system.')

        elif 'screenshot' in text:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken and saved.')

        elif 'search' in text:
            speak('What should I search?')
            query = listen()
            time.sleep(0.3)
            pywhatkit.search(query)
            speak(f'Searching {query} on Google.')
            time.sleep(0.3)

        elif 'translate' in text:
            speak('Say the text to translate.')
            data = listen()
            try:
                translated = translator.translate(data, dest='hi')
                speak(f'Translation in Hindi: {translated.text}')
            except Exception as e:
                print("Translation Error:", e)
                speak("Sorry, translation service is not available right now.")

        elif 'wikipedia' in text:
            topic = text.replace('wikipedia', '').strip() or 'India'
            speak('Searching Wikipedia for ' + topic)
            time.sleep(0.3)
            summary = search_wikipedia(topic)
            speak(summary)
            time.sleep(0.3)

        elif 'joke' in text:
            jokes = [
                "Why do computers hate bugs? Because they can’t debug themselves!",
                "I told my computer I needed a break, and it said — No problem, I’ll sleep!",
                "Why was the computer cold? It left its Windows open!"
            ]
            speak(random.choice(jokes))

        elif 'who made you' in text:
            speak('I was created by Chirag, the future AI master!')

        elif 'how are you' in text:
            speak('I am great, Chirag. Always ready to help you!')

        elif 'exit' in text or 'bye' in text:
            speak('Goodbye!')
            time.sleep(0.3)
            break

        else:
            speak('I can control your PC, play songs, search, and much more.')

if __name__ == '__main__':
    main()
