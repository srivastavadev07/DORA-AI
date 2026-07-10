import subprocess

def open_app(command):

    if "notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    elif "calculator" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    elif "paint" in command:
        subprocess.Popen("mspaint.exe")
        return "Opening Paint."

    return None