from uc1 import Contact
from uc2 import AddressBook

class AddressBookSystem:
    def __init__(self):
        self.books = {}

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