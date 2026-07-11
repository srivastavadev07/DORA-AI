import os
import ctypes


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

    return None