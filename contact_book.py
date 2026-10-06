
import json


class Contact:  # Class to represent one contact

    # Constructor runs automatically when a Contact object is created
    def __init__(self, name, phone, email, address):
        self.name = name       # Store the contact name
        self.phone = phone     # Store the phone number
        self.email = email     # Store the email address
        self.address = address # Store the address

    # Convert a Contact object into a dictionary
    def to_dict(self):
        # Return the contact details as key-value pairs
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }


class ContactBook:  # Class to manage multiple contacts

    # Constructor creates an empty contact list
    def __init__(self):
        self.contacts = []  # List to store Contact objects

    # Method to add a new contact
    def add_contact(self):
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        # Check whether the phone number already exists
        for contact in self.contacts:
            if contact.phone == phone:
                print("Contact with this phone number already exists.")
                return  # Stop if a duplicate phone number is found

        # Create a new Contact object after checking duplicates
        contact = Contact(name, phone, email, address)

        # Add the Contact object to the list
        self.contacts.append(contact)

        print("Contact added successfully.")

    # Method to display all contacts
    def view_contacts(self):
        # Check whether the contact list is empty
        if not self.contacts:
            print("No contacts available.")
            return

        # Go through each contact in the list
        for contact in self.contacts:
            print("\nName:", contact.name)
            print("Phone:", contact.phone)
            print("Email:", contact.email)
            print("Address:", contact.address)

    # Method to search for a contact
    def search_contact(self):
        search = input(
            "Enter name or phone number: "
        ).strip().lower()

        found = False  # Assume no matching contact is found

        # Search using the contact name or phone number
        for contact in self.contacts:
            if (search in contact.name.lower()
                    or search in contact.phone):

                print("\nName:", contact.name)
                print("Phone:", contact.phone)
                print("Email:", contact.email)
                print("Address:", contact.address)

                found = True  # A matching contact was found

        # Check after searching all contacts
        if not found:
            print("Contact not found.")

    # Method to update an existing contact
    def update_contact(self):
        phone = input(
            "Enter phone number of contact to update: "
        ).strip()

        # Search for the contact using its phone number
        for contact in self.contacts:
            if contact.phone == phone:
                contact.name = input("Enter new name: ").strip()
                contact.email = input("Enter new email: ").strip()
                contact.address = input("Enter new address: ").strip()

                print("Contact updated successfully.")
                return  # Stop after updating the contact

        # Display this message only if no contact matches
        print("Contact not found.")

    # Method to delete an existing contact
    def delete_contact(self):
        phone = input(
            "Enter phone number of contact to delete: "
        ).strip()

        # Search for the contact in the list
        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return

        print("Contact not found.")

    # Method to sort contacts alphabetically by name
    def sort_contacts(self):
        self.contacts.sort(
            key=lambda contact: contact.name.lower()
        )

        print("Contacts sorted alphabetically.")
        self.view_contacts()

    # Method to save contacts into a JSON file
    def save_contacts(self):
        data = []  # List to store contact dictionaries

        # Convert each Contact object into a dictionary
        for contact in self.contacts:
            data.append(contact.to_dict())

        # Open the file in write mode
        with open("contacts.json", "w") as file:
            # Write the data into the JSON file
            json.dump(data, file, indent=4)

        print("Contacts saved successfully.")

    # Method to load contacts from a JSON file
    def load_contacts(self):
        try:
            # Open the correct JSON filename in read mode
            with open("contacts.json", "r") as file:
                data = json.load(file)

            # Start with an empty contact list
            self.contacts = []

            # Convert each dictionary into a Contact object
            for contact_data in data:
                contact = Contact(
                    contact_data["name"],
                    contact_data["phone"],
                    contact_data["email"],
                    contact_data["address"]
                )

                # Add the Contact object to the list
                self.contacts.append(contact)

        # If the file doesn't exist, start with an empty list
        except FileNotFoundError:
            self.contacts = []


# Main function to run the application
def main():

    # Create a ContactBook object
    contact_book = ContactBook()

    # Load previously saved contacts
    contact_book.load_contacts()

    # Repeat the menu until the user exits
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

        # Get the user's menu choice
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
            # Save contacts before exiting
            contact_book.save_contacts()
            print("Thank you for using Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run main() when this file is executed directly
if __name__ == "__main__":
    main()    




      

    



















































































































































































