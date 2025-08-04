class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            return True
        return False  # UC6: Prevent duplicate by first name