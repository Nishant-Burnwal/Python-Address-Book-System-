class AddressBook:
    def __init__(self):
        self.contacts = []

    def edit_contact(self, first_name, updated_contact):
        for i, c in enumerate(self.contacts):
            if c.first_name.lower() == first_name.lower():
                self.contacts[i] = updated_contact
                return True
        return False