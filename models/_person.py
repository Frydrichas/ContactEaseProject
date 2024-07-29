from datetime import datetime


class _Person:
    """A class representing a person with a first name, last name, and birthdate."""

    def __init__(self, first_name, last_name, birth, address):
        self._first_name = first_name
        self._last_name = last_name
        self._birth = birth
        self._address = address

    def get_first_name(self):
        """Return the first name of the person"""
        return self._first_name

    def get_last_name(self):
        """Return the last name of the person"""
        return self._last_name

    def get_birth(self):
        """Return the birthdate of the person"""
        return self._birth

    def get_address(self):
        """Return the address of the person"""
        return self._address

    def get_full_name(self):
        """Return the full name of the person"""
        return self._first_name + ' ' + self._last_name

    def get_age(self):
        """Compute and return the age of the person"""
        current_date = datetime.now()
        age = current_date.year - self._birth.year
        if (current_date.month, current_date.day) < (self._birth.month, self._birth.day):
            age -= 1
        return age
