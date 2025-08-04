
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
