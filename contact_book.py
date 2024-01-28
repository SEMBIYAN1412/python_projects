contact_book = {}

#add contact
def add_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    contact_book[name] = phone_number

#search contact
def search_contact():
    name = input("Enter the name to search: ")
    if name in contact_book:
        return contact_book[name]
    else:
        return "Contact not found"

#main program
while True:
    print("""
        1. Add a new contact
        2. Search for a contact
        3. Quit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        print(search_contact())
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
