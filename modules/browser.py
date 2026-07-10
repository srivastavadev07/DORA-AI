import webbrowser

def open_website(command):

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    elif "linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        return "Opening LinkedIn."

    return None