class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.available = True

    def __str__(self):
        status = str("Available" if self.available == True else "Borrowed")
        return f"{self.title} ({self.year}) - {status}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_item(self):
        if self.available == False:
            self.available = True
            return True
        else:
            return False


class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def __str__(self):
        status = str("Available" if self.available == True else "Borrowed")
        return f"{self.title} by {self.author} ({self.year}) - {status}"



class Magazine(LibraryItem):
    def __init__(self, title, year, issue):
        super().__init__(title, year)
        self.issue = issue

    def __str__(self):
        status = str("Available" if self.available == True else "Borrowed")
        return f"{self.title} - Issue {self.issue} ({self.year}) - {status}"

class Library():
    def __init__(self):
        self.libary = []

    def add_item(self, item):
        self.libary.append(item)

    def available_items(self):
        available = []
        for item in self.libary:
            if item.available:
                available.append(item)
        return available

    def borrow_item(self, title):
        for item in self.libary:
            if item.title == title:
                return item.borrow()
        return False

# book = Book("Dune", 1965, "Frank Herbert")
# magazine = Magazine("Python Monthly", 2025, 12)

# print(book)
# # Dune by Frank Herbert (1965) - Available

# print(book.borrow())  # True
# print(book.borrow())  # False

# print(book)
# # Dune by Frank Herbert (1965) - Borrowed

# print(book.return_item())  # True

# print(magazine)
# # Python Monthly - Issue 12 (2025) - Available


# library = Library()

# library.add_item(Book("Dune", 1965, "Frank Herbert"))
# library.add_item(Book("1984", 1949, "George Orwell"))
# library.add_item(Magazine("Python Monthly", 2025, 12))

# print(library.borrow_item("Dune"))  # True
# print(library.borrow_item("Dune"))  # False

# for item in library.available_items():
#     print(item)

# # 1984 by George Orwell (1949) - Available
# # Python Monthly - Issue 12 (2025) - Available