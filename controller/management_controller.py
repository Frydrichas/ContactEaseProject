"""
Controller that exposes the address book management methods to the interface CLI.
It can be extended for a GUI or to support a frontend in a web app.
"""

from service.book_address_manager import *


def handle_add_contact(user,contact):
    """
    Add a new contact to the user's contact list.

    Args:
        user (User): The user to whom the contact will be added.
        contact (Contact): The contact to be added.
    """
    add_contact(user,contact)


def handle_search_contact_by_values(user,search_values):
    """
    Search for a contact in the user's contact list.

        Args:
        user (User): The user to whom the contact will be added.
        search_values (list): The values to search for in the contact list.
    """

    return search_contact_by_values(user,search_values)


def handle_get_contacts_by_user(user):
    """
    Display all contacts in the user's contact list.

    Args:
        user (User): The user whose contacts will be displayed.
    """
    user_contacts = get_contacts_by_user(user)
    return user_contacts


def handle_edit_contact(user, search_values, contact):
    """
        Edit a contact in the user's contact list.

    Args:
        user (User): The user to whom the contact will be added.
        search_values (list): The values to search for in the contact list.
        contact (Contact): The contact to be edited
    """
    edit_contact(user, search_values, contact)
    return contact


def handle_delete_contact(user,search_values):
    """
        Delete a contact from the user's contact list.

    Args:
        user (User): The user from whom the contact will be removed.
        search_values (list): The values to search for in the contact list to remove the contact.
    """
    return delete_contact(user,search_values)
