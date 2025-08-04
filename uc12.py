class AddressBookSystem:
    def __init__(self):
        self.books = {}

    def sort_by_city(self, book_name):
        book = self.books.get(book_name)
        if book:
            return sorted(book.get_all_contacts(), key=lambda c: c.city.lower())
        return []

    def sort_by_state(self, book_name):
        book = self.books.get(book_name)
        if book:
            return sorted(book.get_all_contacts(), key=lambda c: c.state.lower())
        return []

    def sort_by_zip(self, book_name):
        book = self.books.get(book_name)
        if book:
            return sorted(book.get_all_contacts(), key=lambda c: c.zip_code)
        return []