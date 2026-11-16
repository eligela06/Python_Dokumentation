class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.available = True

    def __str__(self):
        if self.available:
            return f"{self.title} ({self.year}) - Available"
        else:
            return f"{self.title} ({self.year}) - Borrowed"

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
        if self.available:
            return f"{self.title} by {self.author} ({self.year}) - Available"
        else:
            return f"{self.title} by {self.author} ({self.year}) - Borrowed"


class Magazine(LibraryItem):
    def __init__(self, title, year, issue):
        super().__init__(title, year)
        self.issue = issue

    def __str__(self):
        if self.available:
            return f"{self.title} - Issue {self.issue} ({self.year}) - Available"
        else:
            return f"{self.title} - Issue {self.issue} ({self.year}) - Borrowed"



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

