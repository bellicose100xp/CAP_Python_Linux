import platform
import os


def clear_terminal():
    system_type = platform.system()
    if system_type == "Windows":
        os.system("cls")
    else:
        os.system("clear")
