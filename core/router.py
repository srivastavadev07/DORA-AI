from modules.apps import open_app
from modules.browser import open_website
from modules.system import system_commands

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

    return None