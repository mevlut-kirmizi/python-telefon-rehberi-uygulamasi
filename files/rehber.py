from phone_class import PhoneBook

pb = PhoneBook()

while True:
    print("\nPhone Book")
    print("1 - Add Contact")
    print("2 - List Contacts")
    print("3 - Delete Contact")
    print("4 - Exit")

    choice = input("Make your choice: ")

    if choice == "1":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        phone = input("Phone Number: ")
        pb.add_contact(first_name, last_name, phone)

    elif choice == "2":
        pb.list_contacts()

    elif choice == "3":
        phone = input("Enter phone number to delete: ")
        pb.delete_contact(phone)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")


    

    
    