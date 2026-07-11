import os
from datetime import datetime
from PIL import ImageGrab

def take_screenshot(command):

    if "screenshot" in command:

        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
        path = os.path.abspath(os.path.join(folder, filename))

        image = ImageGrab.grab()
        image.save(path)

        print("Saved at:", path)
        print("File exists:", os.path.exists(path))

        return f"Screenshot saved as {filename}"

    return None