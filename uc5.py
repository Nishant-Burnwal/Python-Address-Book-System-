from uc2 import AddressBook


class AddressBookSystem:
    def __init__(self):
        self.books = {}

    def add_address_book(self, name):
        if name not in self.books:
            self.books[name] = AddressBook()
            return True
        return False