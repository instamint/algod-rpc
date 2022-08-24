import os
from common import common
from default import default

def get_user_choice():
    print("\n[1] Common")
    print("[2] Default")
    print("[q] Quit.")
    return input("> ")

def get_default():
    print("\n[1] Health")
    print("[2] Get account by Id")
    print("[3] Get asset by Id")
    print("[4] Get transaction by Id")
    print("[5] Get transaction by Id")
    print("[6] Get transaction by Id")
    print("[7] Get transaction by Id")
    print("[8] Get transaction by Id")
    print("[9] Get transaction by Id")
    print("[10] Get transaction by Id")
    print("[q] Quit.")
    return input("> ")

### MAIN PROGRAM ###
choice = ""
os.system("clear")
while choice != "q":    
    choice = get_user_choice()
    if choice == "1":
        common()
    elif choice == "2":
        default()
    elif choice == "q":
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")



