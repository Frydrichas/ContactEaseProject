from ._person import _Person
from .constants import contact_info_group


def _check_contact_info_validity(key):
    """Check if the key is valid"""
    try:
        assert key in contact_info_group, 'Invalid contact information'
    except AssertionError as e:
        print(e)
        return False


class Contact(_Person):
    """A class representing a contact, which is an extension of _Person with contact information."""

    def __init__(self, first_name, last_name, birth, address, contact_note, contact_infos):
        super().__init__(first_name, last_name, birth, address)
        self._contact_note = contact_note
        self._contact_infos = contact_infos

    def get_contact_note(self):
        """Return the contact_note note"""
        return self._contact_note

    def get_contact_infos(self):
        """Return all contact infos"""
        return self._contact_infos

    def get_contact_info(self, key):
        """Return the specific contact info """
        return self._contact_infos[key]

    def to_dict(self):
        """Convert the Contact object to a dictionary."""
        return {
            'first_name': self.get_first_name(),
            'last_name': self.get_last_name(),
            'birth': self.get_birth(),
            'address': self.get_address(),
            'contact_note': self.get_contact_note(),
            'contact_infos': self.get_contact_infos()
        }

    def __repr__(self):
        """Return a string representation of the Contact object."""
        contact_infos = self.get_contact_infos()
        if contact_infos is not None:
            contact_infos_str = '\n'.join([f'\t{key} = {value}' for key, value in contact_infos.items()])
        else:
            contact_infos_str = ""

        return (f"\n"
                f"Contact: \n"
                f" first_name={self.get_first_name()}, \n"
                f" last_name={self.get_last_name()}, \n"
                f" birth={self.get_birth()}, \n"
                f" address={self.get_address()}, \n"
                f" contact_note={self.get_contact_note()}, \n"
                f" contact_infos:\n{contact_infos_str}\n")
