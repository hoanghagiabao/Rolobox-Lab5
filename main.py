import contact 
import os

contacts = []

def read_file():
    try:
        with open("addresses.txt", "r") as file:
            for line in file:
                fn, ln, ph, addr, city, zip = line.strip().split(",")
                new_contact = contact.contact(fn, ln, ph, addr, city, zip)
                contacts.append(new_contact)
    except FileNotFoundError:
        print("No existing contacts file found. Starting with an empty rolodex.")

def write_file():
    with open("contacts.txt", "w") as file:
        for c in contacts:
            file.write(f"{c.first_name}, {c.last_name}, {c.phone}, {c.address}, {c.city}, {c.zip}\n")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_menu_choice():
    print("Rolodex Menu")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Modify Contact")
    print("5. Exit")
    print('number of current contacts:', len(contacts))
    choice = input("Enter your choice: ")
    return choice

    clear_screen()

def modify_contact(c):
    print("Current details:", c)
    fn = input("Enter new first name (leave blank to keep current): ")
    ph = input("Enter new phone number (leave blank to keep current): ")
    addr = input("Enter new address (leave blank to keep current): ")
    city = input("Enter new city (leave blank to keep current): ")
    zip = input("Enter new zip code (leave blank to keep current): ")
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
    print("Contact updated:", c)

def main():
    read_file()
    while True:
        choice = get_menu_choice()
        

        if choice == '1':
            print("Contacts List:")
            contacts.sort()
            for c in contacts:
                print(c)
            
        if choice == '2':
            fn = input("Enter first name: ")
            ln = input("Enter last name: ")
            ph = input("Enter phone number: ")
            addr = input("Enter address: ")
            city = input("Enter city: ")
            zip = input("Enter zip code: ")
            new_contact = contact.contact(fn, ln, ph, addr, city, zip)
            contacts.append(new_contact)
        if choice == '3':
            print("Search Options:")
            print("1. Search by Last Name")
            print("2. Search by Zipcode")
            search_choice = input("Enter your search option: ")
            found = False
            if search_choice == '1':
                ln = input("Enter last name to search: ")
                for c in contacts:
                    if c.last_name == ln:
                        print(c)
                        found = True
            elif search_choice == '2':
                zcode = input("Enter zip code to search: ")
                for c in contacts:
                    if c.zip == zcode:
                        print(c)
                        found = True
            else:
                print("Invalid search option.")
            if not found:
                print("Contact not found.")
        if choice == '4':
            ln = input("Enter last name of contact to modify: ")
            found = False
            for c in contacts:
                if c.last_name == ln:
                    modify_contact(c)
                    found = True
            if not found:
                print("Contact not found.")
        if choice == '5':
            write_file()
            print("Contacts saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()