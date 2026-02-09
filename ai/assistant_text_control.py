import os
import datetime
import webbrowser
from PIL import Image, ImageDraw, ImageFont

# ---------------- SPEAK (TEXT OUTPUT) ----------------

def speak(text):
    print(f"Assistant: {text}")

# ---------------- FILE FUNCTIONS ----------------

def create_file(name):
    with open(f"{name}.txt", "w") as f:
        f.write("New file created by Assistant.\n")
    speak(f"File {name}.txt created successfully.")

def write_file(name):
    text = input("Enter text to write: ")
    with open(f"{name}.txt", "a") as f:
        f.write(text + "\n")
    speak("Text written to file.")

def read_file(name):
    try:
        with open(f"{name}.txt", "r") as f:
            speak(f.read())
    except FileNotFoundError:
        speak("File not found.")

def open_file(name):
    path = os.path.abspath(f"{name}.txt")
    if os.path.exists(path):
        os.startfile(path)
        speak("Opening file.")
    else:
        speak("File not found.")

# ---------------- IMAGE FUNCTIONS ----------------

def generate_image():
    img_name = input("Enter image name: ")
    text = input("Enter text for image: ")

    img = Image.new("RGB", (512, 512), color="white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()

    draw.text((50, 230), text, fill="black", font=font)

    img.save(f"{img_name}.png")
    speak(f"Image {img_name}.png created successfully.")

def open_image():
    name = input("Enter image name: ")
    path = os.path.abspath(f"{name}.png")

    if os.path.exists(path):
        os.startfile(path)
        speak("Opening image.")
    else:
        speak("Image not found.")

# ---------------- SYSTEM FUNCTIONS ----------------

def shutdown_pc():
    speak("Shutting down PC in 5 seconds.")
    os.system("shutdown /s /t 5")

# ---------------- MAIN LOOP ----------------

def main():
    speak("Text based AI Assistant started.")
    speak("Available commands:")
    speak("time, open youtube, open instagram, create file, write, read file, open, generate image, open image, shutdown, exit")

    while True:
        cmd = input("You: ").lower()

        if cmd == "time":
            speak(datetime.datetime.now().strftime("%H:%M:%S"))

        elif cmd == "open youtube":
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif cmd == "open instagram":
            webbrowser.open("https://instagram.com")
            speak("Opening Instagram")

        elif cmd == "create file":
            name = input("Enter filename: ")
            create_file(name)

        elif cmd == "write":
            name = input("Enter filename: ")
            write_file(name)

        elif cmd == "read file":
            name = input("Enter filename: ")
            read_file(name)

        elif cmd == "open":
            name = input("Enter filename: ")
            open_file(name)

        elif cmd == "generate image":
            generate_image()
    
        elif cmd == "open image":
            open_image()

        elif cmd == "shutdown":
            shutdown_pc()
            break

        elif cmd == "exit":
            speak("Goodbye!")
            break

        else:
            speak("Invalid command.")

# ---------------- RUN ----------------

if __name__ == "__main__":
    main()
