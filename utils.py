from sys import platform
from os import system

# clear - Calls the clear command based on the OS
def clear():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        system("clear")
    elif platform == "win32":
        system("cls")
    else:
        print("Platform not implemented")