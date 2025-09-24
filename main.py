"""CECS 277 Classes & Objects
09/24/2025
Group 4
Student 1: Thanh Phat Bui
Student 2: Ha Gia Bao Hoang
Description:
Rolodex
Create a program that allows the user to view, search, and modify a contact list made up of
contact objects. A contact has a name, phone number, address, city, and zip code. Contacts are
initially read in from the file ‘addresses.txt’ and then are written back to the file when the
program ends."""
import contact 
import os

# global list of contact objects
contacts = []

def read_file():
    """
    INPUT:
        - reads from file
    OUTPUT:
        - populates to global 'contacts' list
    """
    try:
        # try to open the file, handle missing file
        with open("addresses.txt", "r") as file:
            for line in file:
                # remove trailing newline and split by commas into 6 pieces
                fn, ln, ph, addr, city, zip = line.strip().split(",")
                # build a contact object from class
                new_contact = contact.contact(fn, ln, ph, addr, city, zip)
                # add to the global list
                contacts.append(new_contact)
                # if file not found, start by empty list
    except FileNotFoundError:
        print("No existing contacts file found. Starting with an empty rolodex.")

def write_file():
    """
    INPUT:
        - global 'contacts'
    OUTPUT:
        - writes to 'contacts.txt'
    """
    with open("contacts.txt", "w") as file:
        for c in contacts:
            # write in file
            file.write(f"{c.first_name}, {c.last_name}, {c.phone}, {c.address}, {c.city}, {c.zip}\n")
#clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_menu_choice():
    """
    INPUT:
        - input choice from user
    OUTPUT:
        - menu choice entered by the user
    """
    # menu
    print("Rolodex Menu")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Modify Contact")
    print("5. Exit")
    # show how many contacts exist
    print('number of current contacts:', len(contacts))
    # user's choice
    choice = input("Enter your choice: ")
    return choice

    clear_screen()

def modify_contact(c):
    # display current contact
    print("Current details:", c)
    # prompt user for new values
    fn = input("Enter new first name (leave blank to keep current): ")
    ph = input("Enter new phone number (leave blank to keep current): ")
    addr = input("Enter new address (leave blank to keep current): ")
    city = input("Enter new city (leave blank to keep current): ")
    zip = input("Enter new zip code (leave blank to keep current): ")
    # apply changes
    if fn:
        c.first_name = fn
    if ph:
        c.phone = ph
    if addr:
        c.address = addr
    if city:
        c.city = city
    if zip:
        c.zip = zip
        # show contact updated
    print("Contact updated:", c)

def main():
    # load data
    read_file()
    while True:
        # show menu and get choice
        choice = get_menu_choice()
        
        # display contacts
        if choice == '1':
            print("Contacts List:")
            # sort
            contacts.sort()
            # print each contact
            for c in contacts:
                print(c)
        # add a new contact
        if choice == '2':
            # get user new contact fields from user
            fn = input("Enter first name: ")
            ln = input("Enter last name: ")
            ph = input("Enter phone number: ")
            addr = input("Enter address: ")
            city = input("Enter city: ")
            zip = input("Enter zip code: ")
            # create new contact object and add to list
            new_contact = contact.contact(fn, ln, ph, addr, city, zip)
            contacts.append(new_contact)
        #search
        if choice == '3':
            # sub-menu
            print("Search Options:")
            # search option by last name
            print("1. Search by Last Name")
            # search option by zip code
            print("2. Search by Zipcode")
            search_choice = input("Enter your search option: ")
            found = False
            if search_choice == '1':
                # choice == 1 search by last name
                ln = input("Enter last name to search: ")
                for c in contacts:
                    if c.last_name == ln:
                        print(c)
                        found = True
            # choice == 2 search by zip code
            elif search_choice == '2':
                zcode = input("Enter zip code to search: ")
                for c in contacts:
                    if c.zip == zcode:
                        print(c)
                        found = True
            # Bad choice
            else:
                print("Invalid search option.")
            # report not found
            if not found:
                print("Contact not found.")
            # modify a contact
        if choice == '4':
            ln = input("Enter last name of contact to modify: ")
            # to track found
            found = False            
            for c in contacts:
                # found, modify contact
                if c.last_name == ln:
                    modify_contact(c)
                    found = True
            # report no contact matched the last name
            if not found:
                print("Contact not found.")
        # exit
        if choice == '5':
            write_file()
            print("Contacts saved. Exiting.")
            break
        # Bad choice
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
