from datetime import datetime

def system_commands(command):

    if "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}"

    return None