
import os

from function import log, get_genesis, get_health, get_version

def get_common_choice():
    print("\n[1] Health - Returns OK if healthy")
    print("[2] Genesis - Gets the genesis information")
    print("[3] Version - Get Version")
    print("[q] Back.")
    return input("> ")

def common():
    os.system("clear")
    common_choice = ""
    while common_choice != "q":
        common_choice = get_common_choice()
        if common_choice == "1":
            log(get_health())
        elif common_choice == "2":
            log(get_genesis())
        elif common_choice == "3":
            log(get_version())    
        elif common_choice == "q":
            os.system("clear")    
        else:
            print("\nI didn't understand that choice.\n")
