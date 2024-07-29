"""
This module contains the welcome function that show the CLI interface and allow login operations
"""

from controller.login_controller import handle_login, handle_register

def welcome():
    """Welcome the user and ask for login or register."""

    print("Welcome to the ContactEase Solution Address Book Application")
    print("Please choose one of the following options:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    option = input("Enter your option: ")

    if option == '3':
        print("Closing session")
        return option, None
    else:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if option == '1':
            user = handle_login(username,password)
        elif option == '2':
            user = handle_register(username,password)
        else:
            print("Closing session")
            return option, None

    return option, user
