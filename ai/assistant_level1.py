import datetime
import webbrowser
import wikipedia

def get_time():
    return datetime.datetime.now().strftime('%H:%M')

def search_wikipedia(query, sentences=2):
    try:
        return wikipedia.summary(query, sentences=sentences)
    except Exception as e:
        return f"Wikipedia error: {e}"

def main():
    print("🤖 Simple Assistant — type 'help' for commands")
    while True:
        cmd = input("You: ").strip().lower()

        if cmd in ("exit", "quit", "stop"):
            print("Goodbye, Pavan!")
            break

        elif cmd == "help":
            print("Commands: time, open youtube, wiki <topic>, exit")

        elif cmd == "time":
            print("⏰ Time:", get_time())

        elif cmd.startswith("open "):
            site = cmd.split(" ", 1)[1]
            if site == "youtube":
                webbrowser.open("https://youtube.com")
                print("Opening YouTube...")

            elif site == "instagram":
               webbrowser.open("https://instagram.com")
               print("Opening Instagram...")
            elif site == "whatsapp":
               webbrowser.open("https://web.whatsapp.com")
               print("Opening Instagram...")
            else:
                print("Unknown site. Try 'open youtube'.")

        elif cmd.startswith("wiki "):
            topic = cmd.split(" ", 1)[1]
            print(search_wikipedia(topic))

        else:
            print("I don’t understand. Type 'help' for commands.")

if __name__ == "__main__":
    main()