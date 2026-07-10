import speech_recognition as sr

recognizer = sr.Recognizer()

# Improve sensitivity

recognizer.dynamic_energy_threshold = True

recognizer.energy_threshold = 40

recognizer.pause_threshold = 0.7

recognizer.non_speaking_duration = 0.2

recognizer.operation_timeout = None
def listen():

    with sr.Microphone() as source:

        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

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