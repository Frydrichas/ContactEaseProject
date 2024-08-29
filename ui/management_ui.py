"""
This module contains the management functions that show the CLI interface and allow contact management operations
"""

import controller.management_controller as mc
from models.contact import Contact
from models.constants import contact_info_group
from datetime import datetime


def _insert_birth_date():
    """
    Insert the birth date in the format dd/mm/yyyy
    """
    inserting = True
    birth_date = None

    while inserting:
        birth_date = input("Enter the birth date (dd/mm/yyyy): ")
        if birth_date == '':
            break
        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
            inserting=False
        except ValueError:
            print("Incorrect data format, should be dd/mm/yyyy")
            continue
    return birth_date


def _insert_contact_infos():
    """
    Insert the contact information
    """
    inserting = True
    contact_infos = {}

    while inserting:
        print(f"Contact info allowed: {contact_info_group} ")
        input_info = input("Enter enter contact info (type:value): ").split(":")

        if input_info is None or input_info == ['']:
            return None

        if len(input_info) != 2:
            print("Invalid contact information")
            continue

        if input_info[0] not in contact_info_group:
            print("Invalid contact information")
            continue
        else:
            contact_infos[input_info[0]] = input_info[1]
            inserting = input("Do you want to add more contact info? (y/n): ")
            if inserting == 'n':
                inserting = False

    return contact_infos


def ui_add_new_contact(user):
    """Add a new contact to the user's contact list."""
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    birth_date = _insert_birth_date()
    address = input("Enter the address: ")
    contact_note = input("Enter the contact note: ")
    contact_infos = _insert_contact_infos()

    contact = Contact(first_name, last_name, birth_date, address, contact_note, contact_infos)
    mc.handle_add_contact(user, contact)
    return contact


def ui_display_all_contacts(user):
    """Display all contacts in the user's contact list."""
    user_contacts = mc.handle_get_contacts_by_user(user)
    return user_contacts


def ui_search_contact(user):
    """Search for a contact in the user's contact list."""
    search_values = input("Enter first name or last name: ").split(" ")
    user_contact = mc.handle_search_contact_by_values(user, search_values)
    return user_contact


def ui_edit_contact(user):
    """Edit a contact in the user's contact list."""
    search_values = input("Enter first name or last name: ").split(" ")
    user_contact = mc.handle_search_contact_by_values(user, search_values)

    if user_contact is not None:
        print(user_contact)
        print("Enter the new values (leave blank to keep the old value)")
        first_name = input("Enter the first name: ") or user_contact.get_first_name()
        last_name = input("Enter the last name: ") or user_contact.get_last_name()
        birth_date = _insert_birth_date or user_contact.get_birth()
        address = input("Enter the address: ") or user_contact.get_address()
        contact_note = input("Enter the contact note: ") or user_contact.get_contact_note()
        contact_infos = _insert_contact_infos()

        if contact_infos is None:
            contact_infos = user_contact.get_contact_infos()

        contact = Contact(first_name, last_name, birth_date, address, contact_note, contact_infos)
        return mc.handle_edit_contact(user, search_values, contact)


def ui_remove_contact(user):
    """
    Delete a contact from the user's contact list.
    """
    fields = input("Enter the value to search: ").split(" ")
    flag = mc.handle_delete_contact(user, fields)
    return flag


def contacts_management(user):
    """Display the menu and ask for the user's choice."""

    print(f"Welcome {user.get_username()}")
    print("Please choose one of the following options: ")
    print("1. Add a new contact ")
    print("2. Display all contact ")
    print("3. Search for a contact ")
    print("4. Edit a contact ")
    print("5. Delete a contact ")
    print("6. Logout ")

    option = input("Enter your option: ")

    if option == '6':
        print("Closing session")
        return -1
    else:
        if option == '1':
            contact = ui_add_new_contact(user)
            print(contact)
        elif option == '2':
            contacts = ui_display_all_contacts(user)
            if contacts:
                print(contacts)
            else:
                print("No contacts found")
        elif option == '3':
            contact = ui_search_contact(user)
            if contact:
                print(contact)
            else:
                print("Contact not found")
        elif option == '4':
            contact = ui_edit_contact(user)
            if contact:
                print(contact)
            else:
                print("Contact not found")
        elif option == '5':
            if ui_remove_contact(user):
                print("Contact deleted")
            else:
                print("Contact not found")
        else:
            print("Closing session")
            return -1

        return 1
