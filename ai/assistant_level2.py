import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # speaking speed

# Initialize speech recognizer
r = sr.Recognizer()

def speak(text):
    print('Assistant:', text)
    engine.say(text)
    engine.runAndWait()

def listen(timeout=6, phrase_time_limit=6):
    try:
        with sr.Microphone() as source:
            print('Listening... speak now!')
            r.adjust_for_ambient_noise(source, duration=0.6)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        text = r.recognize_google(audio, language='en-in')
        print('You:', text)
        return text.lower()
    except:
        return ''

def get_time():
    return datetime.datetime.now().strftime('%H:%M')

def search_wikipedia(query, sentences=2):
    try:
        return wikipedia.summary(query, sentences=sentences)
    except:
        return "Sorry, Wikipedia didn't return results."

def main():
    speak('Hello Chirag — I am your voice assistant. Say a command.')

    while True:
        text = listen()
        if not text:
            speak('I did not catch that. Please repeat.')
            continue

        if 'time' in text:
            speak('The time is ' + get_time())

        elif 'open youtube' in text:
            webbrowser.open('https://youtube.com')
            speak('Opening YouTube')

        elif 'open whatsapp' in text:
            webbrowser.open('https://web.whatsapp.com')
            speak('Opening WhatsApp Web')

        elif 'open instagram' in text:
            webbrowser.open('https://instagram.com')
            speak('Opening Instagram')

        elif 'wikipedia' in text:
            topic = text.replace('wikipedia', '').strip() or 'India'
            speak('Searching Wikipedia for ' + topic)
            summary = search_wikipedia(topic)
            speak(summary)

        elif 'exit' in text or 'stop' in text:
            speak('Goodbye!')
            break

        else:
            speak("I can do: time, open youtube, open whatsapp, open instagram, wikipedia <topic>, exit")

if __name__ == '__main__':
    main()
