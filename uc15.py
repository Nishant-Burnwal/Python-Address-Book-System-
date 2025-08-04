import json

from uc1 import Contact
from uc2 import AddressBook

class AddressBookSystem:
    def __init__(self):
        self.books = {}

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

