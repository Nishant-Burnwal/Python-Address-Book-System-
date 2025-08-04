class AddressBookSystem:
    def __init__(self):
        self.books = {}

    def count_by_city(self):
        city_map = self.view_by_city()
        return {city: len(contacts) for city, contacts in city_map.items()}

    def count_by_state(self):
        state_map = self.view_by_state()
        return {state: len(contacts) for state, contacts in state_map.items()}