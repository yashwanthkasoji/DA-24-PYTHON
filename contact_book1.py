import json


class Contact:

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }


class ContactBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        for contact in self.contacts:
            if contact.phone == phone:
                print("Contact with this phone number already exists.")
                return

        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        for contact in self.contacts:
            print("\nName:", contact.name)
            print("Phone:", contact.phone)
            print("Email:", contact.email)
            print("Address:", contact.address)

    def search_contact(self):
        search = input("Enter name or phone number: ").strip().lower()
        found = False

        for contact in self.contacts:
            if (search in contact.name.lower() or
                    search in contact.phone):
                print("\nName:", contact.name)
                print("Phone:", contact.phone)
                print("Email:", contact.email)
                print("Address:", contact.address)
                found = True

        if not found:
            print("Contact not found.")

    def update_contact(self):
        phone = input(
            "Enter phone number of contact to update: "
        ).strip()

        for contact in self.contacts:
            if contact.phone == phone:
                contact.name = input("Enter new name: ").strip()
                contact.email = input("Enter new email: ").strip()
                contact.address = input("Enter new address: ").strip()
                print("Contact updated successfully.")
                return

        print("Contact not found.")

    def delete_contact(self):
        phone = input(
            "Enter phone number of contact to delete: "
        ).strip()

        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return

        print("Contact not found.")

    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.name.lower())
        print("Contacts sorted alphabetically.")
        self.view_contacts()

    def save_contacts(self):
        data = []

        for contact in self.contacts:
            data.append(contact.to_dict())

        with open("contacts.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Contacts saved successfully.")

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)

            self.contacts = []

            for contact_data in data:
                contact = Contact(
                    contact_data["name"],
                    contact_data["phone"],
                    contact_data["email"],
                    contact_data["address"]
                )
                self.contacts.append(contact)

        except FileNotFoundError:
            self.contacts = []


def main():
    contact_book = ContactBook()
    contact_book.load_contacts()

    while True:
        print("\n========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Sort Contacts")
        print("7. Save Contacts")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            contact_book.add_contact()

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            contact_book.search_contact()

        elif choice == "4":
            contact_book.update_contact()

        elif choice == "5":
            contact_book.delete_contact()

        elif choice == "6":
            contact_book.sort_contacts()

        elif choice == "7":
            contact_book.save_contacts()

        elif choice == "8":
            contact_book.save_contacts()
            print("Thank you for using Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()