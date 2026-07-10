from core.speech import speak
from core.listen import listen
from core.router import route_command
import time

def main():

    speak("Hello Devansh. DORA AI is online.")

    while True:

        command = listen()

        if not command:
            continue

        print(f"\nCommand: {command}")

        if "stop" in command or "exit" in command:
            speak("Goodbye Devansh. Have a great day.")
            break

        response = route_command(command)

        if response:
            speak(response)
        else:
            speak("Sorry, I don't know that command yet.")

        time.sleep(0.5)

if __name__ == "__main__":
    main()





    