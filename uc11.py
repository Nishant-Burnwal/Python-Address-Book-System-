class AddressBookSystem:
    def __init__(self):
        self.books = {}
    
    def sort_by_name(self, book_name):
        book = self.books.get(book_name)
        if book:
            return sorted(book.get_all_contacts(), key=lambda c: c.first_name.lower())
        return []