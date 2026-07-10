import speech_recognition as sr

recognizer = sr.Recognizer()

# Improve sensitivity
recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8

def listen():

    with sr.Microphone() as source:

        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=2)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:
            return ""

    try:
        command = recognizer.recognize_google(audio)

        print(f"👤 You: {command}")

        return command.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        print("Speech Recognition service unavailable.")
        return ""