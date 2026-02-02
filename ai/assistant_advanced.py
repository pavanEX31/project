import pyttsx3, speech_recognition as sr, os, wikipedia, datetime, webbrowser, pywhatkit, pyautogui, psutil
from googletrans import Translator

engine = pyttsx3.init()
engine.setProperty('rate', 165)
r = sr.Recognizer()
translator = Translator()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio, language='en-in')
        print("You:", cmd)
        return cmd.lower()
    except:
        speak("Sorry, I didn’t catch that.")
        return ""

def create_file(name):
    with open(f"{name}.txt", "w") as f:
        f.write("New file created by AI Assistant.\n")
    speak(f"File {name}.txt created successfully.")

def shutdown_pc():
    speak("Shutting down your PC.")
    os.system("shutdown /s /t 5")

def translate_text(text, dest_lang="hi"):
    translated = translator.translate(text, dest=dest_lang)
    speak(f"Translation: {translated.text}")
    return translated.text

def read_text(file):
    try:
        with open(file, "r") as f:
            data = f.read()
        speak(data)
    except FileNotFoundError:
        speak("File not found.")

def main():
    speak("Hello, I am your upgraded assistant.")
    while True:
        cmd = listen()

        if "time" in cmd:
            speak(datetime.datetime.now().strftime("%H:%M"))

        elif "open youtube" in cmd:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif "open instagram" in cmd:
            webbrowser.open("https://instagram.com")
            speak("Opening Instagram")

        elif "open whatsapp" in cmd:
            webbrowser.open("https://web.whatsapp.com")
            speak("Opening WhatsApp Web")

        elif "create file" in cmd:
            speak("What should I name the file?")
            name = listen()
            create_file(name)

        elif "shutdown" in cmd:
            shutdown_pc()
            break

        elif "translate" in cmd:
            speak("Say the text to translate")
            text = listen()
            translate_text(text, "hi")

        elif "read" in cmd:
            speak("Tell me the filename")
            fname = listen()
            read_text(f"{fname}.txt")

        elif "exit" in cmd or "stop" in cmd:
            speak("Goodbye!")
            break

        else:
            speak("I can control your PC, translate, read files, and more.")

if __name__ == "__main__":
    main()
