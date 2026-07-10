from core.speech import speak
from core.listen import listen
from core.router import route_command
from core.responses import get_thinking_response
import time


def main():

    speak("Hello Devansh. DORA AI is online.")

    while True:

        command = listen()

        if not command:
            continue

        print(f"\n👤 You: {command}")

        if "stop" in command or "exit" in command:
            speak("Goodbye Devansh. Have a great day.")
            break

        # Speak only for AI questions
        if not (
            "open" in command
            or "time" in command
            or "stop" in command
            or "exit" in command
        ):
            speak(get_thinking_response())

        response = route_command(command)

        print(f"\n🤖 DORA:\n{response}")

        spoken_response = response[:250]

        if len(response) > 250:
            spoken_response += " ... Please check the terminal for more details."

        speak(spoken_response)

        time.sleep(0.5)


if __name__ == "__main__":
    main()