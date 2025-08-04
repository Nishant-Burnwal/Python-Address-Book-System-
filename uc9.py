from uc2 import AddressBook

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