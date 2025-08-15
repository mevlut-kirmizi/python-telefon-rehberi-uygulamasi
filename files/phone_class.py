import os

class PhoneBook:
    FILE_NAME = "files/phonebook.txt"

    def __init__(self):
        if not os.path.exists("files"):
            os.makedirs("files")
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w", encoding="utf-8"):
                pass

    def add_contact(self, first_name, last_name, phone):
        with open(self.FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{first_name},{last_name},{phone}\n")
        print(f"{first_name} {last_name} has been added.")

    def list_contacts(self):
        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            contacts = f.readlines()
        if not contacts:
            print("No contacts found.")
        for contact in contacts:
            first_name, last_name, phone = contact.strip().split(",")
            print(f"{first_name} {last_name} - {phone}")

    def delete_contact(self, phone_number):
        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            contacts = f.readlines()
        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            deleted = False
            for contact in contacts:
                if phone_number not in contact:
                    f.write(contact)
                else:
                    deleted = True
        if deleted:
            print(f"Contact with phone number {phone_number} deleted.")
        else:
            print("Contact not found.")

            
            
            
            
            