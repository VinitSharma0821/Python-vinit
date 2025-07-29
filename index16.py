contacts = []
def add_contact():
    name = input("Enter Name: ")
    number = int(input("Enter Number: "))
    contacts.append({
        "name": name,
        "Number": number
    })
    print("Contact added successfully!\n")
def display_all_contacts():
    if not contacts:
        print("No students available.\n")
        return
    print("\nList of Contacts:")
    for c in contacts:
        print(f"Name: {c['name']}, Number: {c['Number']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    for c in contacts:
        if c['name'] == name:
            print(c["name"])
            print(c["Number"])
            print("Contact Found!\n")
            return
    print("Contact not found!\n")

while True:
    print("1, Add Contact")
    print("2, Display all contacts")
    print("3, Search from contact list")

    option = int(input("choose your option: "))

    if option == 1:
        print("Add Contact selected")
        add_contact()
    elif option == 2:
        print("Display contacts selected")
        display_all_contacts()
    elif option == 3:
        search_contact()
    elif option == 4:
        print("Program exited!")
        break
    else:
        print("invalid number")
        break
