
import os

from function import get_application_by_address, get_asset_by_address, get_pending_transaction, get_status, get_transaction_params, log, get_account_by_address, post_transaction


def get_default_choice():
    print("\n[1] Status - Gets the current node status")
    print("[2] Get account information")
    print("[3] Get application information")
    print("[4] Get asset information")
    print("--------- TRANSACTION ----------")
    print("[5] Get parameters for constructing a new transaction")
    print("[6] Broadcasts a raw transaction to the network")
    print("[7] Get a specific pending transaction")
    print("[q] Quit.")
    return input("> ")


def default():
    os.system("clear")
    default_choice = ""
    while default_choice != "q":
        default_choice = get_default_choice()
        if default_choice == "1":
            log(get_status())
        elif default_choice == "2":
            address = input("Account: ")
            log(get_account_by_address(address))
        elif default_choice == "3":
            address = input("Appilcation: ")
            log(get_application_by_address(address))
        elif default_choice == "4":
            address = input("Asset: ")
            log(get_asset_by_address(address))
        elif default_choice == "5":
            log(get_transaction_params())
        elif default_choice == "6":
            rawtxn = input("rawtxn: ")
            log(post_transaction(rawtxn))
        elif default_choice == "7":
            tx_id = input("Transaction: ")
            log(get_pending_transaction(tx_id))
        elif default_choice == "q":
            os.system("clear")
        else:
            print("\nI didn't understand that choice.\n")
