"""
This is the main file of the application. It is the entry point of the application.
"""

from ui.welcome_ui import welcome
from ui.management_ui import contacts_management


def main():
    execute = True
    user = None
    while execute:
        if user is None:
            option, user = welcome()

        if option == "3":
            break

        if user is not None:
            management_result = contacts_management(user)
            if management_result == -1:
                user = None

        execute = False

        res = input("Do you want to continue? (y/n) ")
        if res == 'y':
            execute = True


if __name__ == '__main__':
    main()
