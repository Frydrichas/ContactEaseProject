"""functions to manage the book address actions"""

import json
from typing import List
from models import Contact


def _load_contacts(user) -> List[Contact]:
    """
    Load contact list from json file.

    Args:
        user: the user of whom the contacts are loaded.
    """
    try:
        file_path = f"data/{user.get_username()}-contacts.json"
        with open(file_path, "r") as file:
            contacts_data = json.load(file)

            contacts = []
            for contact_data in contacts_data:
                contact = Contact(
                    first_name=contact_data.get("first_name"),
                    last_name=contact_data.get("last_name"),
                    birth=contact_data.get("birth"),
                    address=contact_data.get("address"),
                    contact_note=contact_data.get("contact_note"),
                    contact_infos=contact_data.get("contact_infos")
                )
                contacts.append(contact)

        return contacts
    except FileNotFoundError:
        print(f" File {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error in json decoding")
        return []


def _write_contacts(user, contacts):
    """
    Write the contacts to the json file.

    Args:
        user: the user of whom the contacts are written.
        contacts: the contacts to write
    """
    try:
        file_path = f"data/{user.get_username()}-contacts.json"
        with open(file_path, 'w') as file:
            json.dump([c.to_dict() for c in contacts], file, indent=4)
        print(f"Operation complete")
    except IOError as e:
        print(f"Error during write on file: {e}")
        return False

    return True


def _is_searched_contact(contact, search_values):
    """
    Check if the contact is the searched contact.

    Args:
        contact: the contact to check.
        search_values: the values to search for.
    """
    if (contact.get_first_name() in search_values and contact.get_last_name() in search_values):
        return True
    elif (contact.get_last_name() in search_values):
        return True
    elif (contact.get_first_name() in search_values):
        return True
    return False


def get_contacts_by_user(user) -> List[Contact]:
    """
    Return the contacts of a user

    Args:
        user: the user of whom the contacts are returned.
    """
    return _load_contacts(user)


def add_contact(user, contact):
    """
    Add a new contact to the user's contact list.

    Args:
        user: the user to add the contact to.
        contact: the contact to add.
        """
    contact_list = _load_contacts(user)
    contact_list.append(contact)
    return _write_contacts(user, contact_list)


def search_contact_by_values(user, search_values):
    """
    Search for the first contact that match the search_values.

    Args:
        user: the user to search the contact in.
        search_values: the values to search for.
    """
    user_contacts = get_contacts_by_user(user)
    for contact in user_contacts:
        if _is_searched_contact(contact, search_values):
            return contact
    return None


def remove_contact_by_values(user, search_values):
    """
    Search for the first contact that match the search_values and remove it from the list.

    Args:
        user: the user to search the contact in.
        search_values: the values to search for.
    """
    user_contacts = get_contacts_by_user(user)
    for contact in user_contacts:
        if _is_searched_contact(contact, search_values):
            user_contacts.remove(contact)
            return user_contacts
    return None


def delete_contact(user, search_values):
    """
    Delete a contact that match the search_values.

    Args:
        user: the user to delete the contact from.
        search_values: the values to search for.
    """
    user_contacts = remove_contact_by_values(user, search_values)
    if user_contacts is None:
        return False

    return _write_contacts(user, user_contacts)


def edit_contact(user, search_values, contact):
    """
    Edit a contact.

    Args:
        user: the user to edit the contact from.
        search_values: the values to search for.
        contact: the contact to edit.
    """
    user_contacts = remove_contact_by_values(user, search_values)
    if user_contacts is None:
        return False
    user_contacts.append(contact)

    return _write_contacts(user, user_contacts)
