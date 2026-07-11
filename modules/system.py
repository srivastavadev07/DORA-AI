import os
import ctypes
from datetime import datetime


def system_commands(command):

    if "lock" in command:
        ctypes.windll.user32.LockWorkStation()
        return "Locking your computer."

    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down your computer."

    elif "restart" in command:
        os.system("shutdown /r /t 1")
        return "Restarting your computer."

    elif "sleep" in command:
        os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
        return "Putting your computer to sleep."

    elif any(word in command for word in ["time", "clock"]):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

    elif any(word in command for word in ["date", "today"]):
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today is {current_date}"

    return None