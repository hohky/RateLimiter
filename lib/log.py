from lib.common import *

def error(message):
    message = f"{c.RESET}[{c.RED}-{c.RESET}] {message}"
    return message


def warning(message):
    message = f"{c.RESET}[{c.LIGHTYELLOW_EX}!{c.RESET}] {message}"
    return message

def sending(message):
    message = f"[{c.LIGHTGREEN_EX}Sending{c.RESET}] {message}"
    return message