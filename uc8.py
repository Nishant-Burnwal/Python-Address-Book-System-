class AddressBookSystem:
    def __init__(self):
        self.books = {}

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
