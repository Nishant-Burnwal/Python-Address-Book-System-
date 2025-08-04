import csv

from uc1 import Contact
from uc2 import AddressBook

class AddressBookSystem:
    def __init__(self):
        self.books = {}

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