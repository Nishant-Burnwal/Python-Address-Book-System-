import re
import csv
import json

print("Welcome to Address Book Program in AddressBookMain class on Master Branch")

# UC1: Create Contact Class
class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __eq__(self, other):
        return self.first_name.lower() == other.first_name.lower()

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Address: {self.address}, City: {self.city}, State: {self.state} - {self.zip_code}, Phone: {self.phone}, Email: {self.email}"

# UC2 - UC6: Manage contacts inside AddressBook
class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            return True
        return False  # UC6: Prevent duplicate by first name

    def edit_contact(self, first_name, updated_contact):
        for i, c in enumerate(self.contacts):
            if c.first_name.lower() == first_name.lower():
                self.contacts[i] = updated_contact
                return True
        return False

    def delete_contact(self, first_name):
        for i, c in enumerate(self.contacts):
            if c.first_name.lower() == first_name.lower():
                del self.contacts[i]
                return True
        return False

    def get_all_contacts(self):
        return self.contacts

# UC5 - UC12: Manage multiple address books and operations
class AddressBookSystem:
    def __init__(self):
        self.books = {}

    def add_address_book(self, name):
        if name not in self.books:
            self.books[name] = AddressBook()
            return True
        return False

    def get_book(self, name):
        return self.books.get(name)

    def search_by_city(self, city):
        results = []
        for book_name, book in self.books.items():
            for c in book.get_all_contacts():
                if c.city.lower() == city.lower():
                    results.append((book_name, c))
        return results

    def search_by_state(self, state):
        results = []
        for book_name, book in self.books.items():
            for c in book.get_all_contacts():
                if c.state.lower() == state.lower():
                    results.append((book_name, c))
        return results

    def view_by_city(self):
        city_map = {}
        for book in self.books.values():
            for c in book.get_all_contacts():
                city_map.setdefault(c.city, []).append(c)
        return city_map

    def view_by_state(self):
        state_map = {}
        for book in self.books.values():
            for c in book.get_all_contacts():
                state_map.setdefault(c.state, []).append(c)
        return state_map

    def count_by_city(self):
        city_map = self.view_by_city()
        return {city: len(contacts) for city, contacts in city_map.items()}

    def count_by_state(self):
        state_map = self.view_by_state()
        return {state: len(contacts) for state, contacts in state_map.items()}

    def sort_by_name(self, book_name):
        book = self.books.get(book_name)
        if book:
            return sorted(book.get_all_contacts(), key=lambda c: c.first_name.lower())
        return []

    def sort_by_city(self, book_name):
        book = self.books.get(book_name)
        if book:
            return sorted(book.get_all_contacts(), key=lambda c: c.city.lower())
        return []

    def sort_by_state(self, book_name):
        book = self.books.get(book_name)
        if book:
            return sorted(book.get_all_contacts(), key=lambda c: c.state.lower())
        return []

    def sort_by_zip(self, book_name):
        book = self.books.get(book_name)
        if book:
            return sorted(book.get_all_contacts(), key=lambda c: c.zip_code)
        return []
    
    # UC: 13 Read and Write the address book with Person Contact into a File using File IO
    def write_to_file(self, book_name, filename):
        book = self.books.get(book_name)
        if not book:
            return False
        with open(filename, 'w', encoding='utf-8') as f:
            for c in book.get_all_contacts():
                line = "|".join([
                    c.first_name, c.last_name, c.address,
                    c.city, c.state, c.zip_code,
                    c.phone, c.email
                ])
                f.write(line + '\n')
        return True

    def read_from_file(self, book_name, filename):
        if book_name not in self.books:
            self.books[book_name] = AddressBook()
        book = self.books[book_name]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    fields = line.strip().split('|')
                    if len(fields) == 8:
                        contact = Contact(*fields)
                        book.add_contact(contact)
            return True
        except FileNotFoundError:
            return False

    # UC 14: Read/Write the Address Book with Persons Contact as CSV File
    def write_to_csv(self, book_name, filename):
        book = self.books.get(book_name)
        if not book:
            return False
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["First Name", "Last Name", "Address", "City", "State", "Zip", "Phone", "Email"])
            for c in book.get_all_contacts():
                writer.writerow([
                    c.first_name, c.last_name, c.address,
                    c.city, c.state, c.zip_code,
                    c.phone, c.email
                ])
        return True

    def read_from_csv(self, book_name, filename):
        if book_name not in self.books:
            self.books[book_name] = AddressBook()
        book = self.books[book_name]
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    contact = Contact(
                        row["First Name"],
                        row["Last Name"],
                        row["Address"],
                        row["City"],
                        row["State"],
                        row["Zip"],
                        row["Phone"],
                        row["Email"]
                    )
                    book.add_contact(contact)
            return True
        except (FileNotFoundError, KeyError):
            return False


    def export_to_txt(self, book_name, filename):
        book = self.books.get(book_name)
        if not book:
            return False
        with open(filename, 'w', encoding='utf-8') as f:
            for c in book.get_all_contacts():
                f.write(str(c) + '\n')
        return True
    # UC 15: Read and Write the Address Book with Person JSON File
    def write_to_json(self, book_name, filename):
        book = self.books.get(book_name)
        if not book:
            return False
        contacts_data = []
        for c in book.get_all_contacts():
            contacts_data.append({
                "first_name": c.first_name,
                "last_name": c.last_name,
                "address": c.address,
                "city": c.city,
                "state": c.state,
                "zip_code": c.zip_code,
                "phone": c.phone,
                "email": c.email
            })
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(contacts_data, f, indent=4)
        return True

    def read_from_json(self, book_name, filename):
        if book_name not in self.books:
            self.books[book_name] = AddressBook()
        book = self.books[book_name]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                contacts_data = json.load(f)
                for data in contacts_data:
                    contact = Contact(
                        data["first_name"],
                        data["last_name"],
                        data["address"],
                        data["city"],
                        data["state"],
                        data["zip_code"],
                        data["phone"],
                        data["email"]
                    )
                    book.add_contact(contact)
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return False


# UC12: Console Input
def get_contact_input():

    def get_valid_phone():
        while True:
            phone = input("Phone Number (10 digits starting with 6-9): ")
            if re.fullmatch(r"^[6-9]\d{9}$", phone):
                return phone
            print("Invalid phone number format. Please enter a valid 10-digit number starting with 6-9.")

    def get_valid_email():
        while True:
            email = input("Email (e.g., abc@example.com): ")
            if re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
                return email
            print("Invalid email format. Please enter a valid email address.")

    return Contact(
        input("First Name: "),
        input("Last Name: "),
        input("Address: "),
        input("City: "),
        input("State: "),
        input("Zip Code: "),
        get_valid_email(),
        get_valid_phone()

    )

# Console UI
def main():
    system = AddressBookSystem()

    while True:
        print("\nMenu:")
        print("1. Add Address Book")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. View Contacts")
        print("6. Search by City")
        print("7. Search by State")
        print("8. View by City")
        print("9. View by State")
        print("10. Count by City")
        print("11. Count by State")
        print("12. Sort by Name")
        print("13. Sort by City")
        print("14. Sort by State")
        print("15. Sort by Zip")
        print("16. Save Address Book to Text File")
        print("17. Load Address Book from Text File")
        print("18. Save Address Book to Text File")
        print("19. Save Address Book to CSV File")
        print("20. Load Address Book from CSV File")
        print("21. Save Address Book to JSON File")
        print("22. Load Address Book from JSON File")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter new Address Book name: ")
            if system.add_address_book(name):
                print("Address Book Added.")
            else:
                print("Address Book already exists.")

        elif choice == '2':
            book_name = input("Enter Address Book name: ")
            book = system.get_book(book_name)
            if book:
                contact = get_contact_input()
                if book.add_contact(contact):
                    print("Contact added.")
                else:
                    print("Duplicate contact not allowed.")
            else:
                print("Book not found.")

        elif choice == '3':
            book_name = input("Enter Address Book name: ")
            book = system.get_book(book_name)
            if book:
                fname = input("Enter First Name to edit: ")
                updated = get_contact_input()
                if book.edit_contact(fname, updated):
                    print("Contact updated.")
                else:
                    print("Contact not found.")
            else:
                print("Book not found.")

        elif choice == '4':
            book_name = input("Enter Address Book name: ")
            book = system.get_book(book_name)
            if book:
                fname = input("Enter First Name to delete: ")
                if book.delete_contact(fname):
                    print("Contact deleted.")
                else:
                    print("Contact not found.")
            else:
                print("Book not found.")

        elif choice == '5':
            book_name = input("Enter Address Book name: ")
            book = system.get_book(book_name)
            if book:
                for c in book.get_all_contacts():
                    print(c)
            else:
                print("Book not found.")

        elif choice == '6':
            city = input("Enter city to search: ")
            results = system.search_by_city(city)
            for book, contact in results:
                print(f"[{book}] {contact}")

        elif choice == '7':
            state = input("Enter state to search: ")
            results = system.search_by_state(state)
            for book, contact in results:
                print(f"[{book}] {contact}")

        elif choice == '8':
            city_map = system.view_by_city()
            for city, people in city_map.items():
                print(f"{city}:")
                for c in people:
                    print(f"  {c}")

        elif choice == '9':
            state_map = system.view_by_state()
            for state, people in state_map.items():
                print(f"{state}:")
                for c in people:
                    print(f"  {c}")

        elif choice == '10':
            counts = system.count_by_city()
            for city, count in counts.items():
                print(f"{city}: {count}")

        elif choice == '11':
            counts = system.count_by_state()
            for state, count in counts.items():
                print(f"{state}: {count}")

        elif choice == '12':
            book_name = input("Enter book to sort by name: ")
            for c in system.sort_by_name(book_name):
                print(c)

        elif choice == '13':
            book_name = input("Enter book to sort by city: ")
            for c in system.sort_by_city(book_name):
                print(c)

        elif choice == '14':
            book_name = input("Enter book to sort by state: ")
            for c in system.sort_by_state(book_name):
                print(c)

        elif choice == '15':
            book_name = input("Enter book to sort by zip: ")
            for c in system.sort_by_zip(book_name):
                print(c)

        elif choice == '16':
            book_name = input("Enter Address Book name: ")
            filename = input("Enter filename to save (e.g., book.txt): ")
            if system.write_to_file(book_name, filename):
                print("Address Book saved to file successfully.")
            else:
                print("Book not found or failed to save.")

        elif choice == '17':
            book_name = input("Enter Address Book name to load into: ")
            filename = input("Enter filename to read (e.g., book.txt): ")
            if system.read_from_file(book_name, filename):
                print("Address Book loaded from file successfully.")
            else:
                print("Failed to read file.")

        elif choice == '19':
            book_name = input("Enter Address Book name: ")
            filename = input("Enter CSV filename (e.g., contacts.csv): ")
            if system.write_to_csv(book_name, filename):
                print("Address Book saved to CSV successfully.")
            else:
                print("Book not found or failed to save.")

        elif choice == '20':
            book_name = input("Enter Address Book name to load into: ")
            filename = input("Enter CSV filename (e.g., contacts.csv): ")
            if system.read_from_csv(book_name, filename):
                print("Address Book loaded from CSV successfully.")
            else:
                print("Failed to read CSV file.")

        elif choice == '21':
            book_name = input("Enter Address Book name: ")
            filename = input("Enter JSON filename (e.g., contacts.json): ")
            if system.write_to_json(book_name, filename):
                print("Address Book saved to JSON successfully.")
            else:
                print("Book not found or failed to save.")

        elif choice == '22':
            book_name = input("Enter Address Book name to load into: ")
            filename = input("Enter JSON filename (e.g., contacts.json): ")
            if system.read_from_json(book_name, filename):
                print("Address Book loaded from JSON successfully.")
            else:
                print("Failed to read JSON file.")



        elif choice == '0':
            print("Exiting Address Book System.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
