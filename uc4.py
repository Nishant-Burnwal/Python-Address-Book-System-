class AddressBook:
    def __init__(self):
        self.contacts = []

    def delete_contact(self, first_name):
        for i, c in enumerate(self.contacts):
            if c.first_name.lower() == first_name.lower():
                del self.contacts[i]
                return True
        return False
