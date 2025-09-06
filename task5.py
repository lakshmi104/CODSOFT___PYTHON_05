contacts = [] 
def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact Added Successfully!")
def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No Contacts Available.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if contact['name'] == keyword or contact['phone'] == keyword:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("Contact Not Found.")
def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            print("What do you want to update?")
            print("1. Phone")
            print("2. Email")
            print("3. Address")
            choice = input("Enter choice (1-3): ")
            if choice == "1":
                contact['phone'] = input("Enter new phone number: ")
            elif choice == "2":
                contact['email'] = input("Enter new email: ")
            elif choice == "3":
                contact['address'] = input("Enter new address: ")
            else:
                print("Invalid Choice.")
                return
            print("Contact Updated Successfully!")
            return
    print("Contact Not Found.")
def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact Deleted Successfully!")
            return
    print("Contact Not Found.")
def contact_book():
    print("📖 CONTACT BOOK 📖")
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\n✅ CONTACT BOOK CLOSED SUCCESSFULLY ✅")
            break
        else:
            print("Invalid Choice. Please try again.")
contact_book()
