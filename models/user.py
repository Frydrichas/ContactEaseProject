import json


def _load_users():
    """load user list from json file."""
    try:
        file_path = "data/users.json"
        with open(file_path, "r") as file:
            users = json.load(file)
        return users
    except FileNotFoundError:
        print(f" File {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error in json decoding")
        return []


class User:
    """
    A class representing the user of the application and allowing to register and login.
    """

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def _user_index(self, users):
        """Return the index of a user in a list."""
        for i, user in enumerate(users):
            if user["username"] == self._username:
                return i
        return -1

    def register(self):
        """Add the user to the Json file."""
        users = _load_users()
        i = self._user_index(users)

        if i >= 0:
            print("Username already existing!")
            return False

        users.append({"username": self._username, "password": self._password})
        try:
            file_path = "data/users.json"
            with open(file_path, 'w') as file:
                json.dump(users, file, indent=4)
            print(f"Registration complete")
        except IOError as e:
            print(f"Error during registration: {e}")
            return False

        file.close()
        return True

    def login(self):
        """Verify user login credential."""
        users = _load_users()
        i = self._user_index(users)
        if i >= 0:
            if users[i]["password"] == self._password:
                return True

        print("Wrong credential!")
        return False

    def get_username(self):
        """Return the username"""
        return self._username
