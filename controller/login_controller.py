"""
Controller that exposes the login methods to the interface CLI.
It can be extended for a GUI or to support a frontend in a web app.
"""

from models import User


def handle_login(username,password):
    """
    Login the user with the given username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    """

    user = User(username,password)
    if user.login():
        return user
    else:
        return None


def handle_register(username, password):
    """
    Register a new user with the given username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    """

    user = User(username, password)
    if user.register():
        return user
    else:
        return None

