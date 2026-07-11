from modules.apps import open_app
from modules.browser import open_website
from modules.system import system_commands
from ai.gemini import ask_gemini
from modules.screenshot import take_screenshot
import ctypes


def route_command(command):

    response = open_app(command)

    if response:
        return response

    response = open_website(command)

    if response:
        return response

    response = system_commands(command)
    if response:
        return response
    
    response = take_screenshot(command)
    if response:
        return response
    
    # If no command matches, ask Gemini
    return ask_gemini(command)