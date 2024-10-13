class Book:
    """Base class to represent a book."""
    
    def __init__(self, title, author):
        """Initialize book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Class to represent an eBook which inherits from Book."""
    
    def __init__(self, title, author, file_size):
        """Initialize eBook attributes, including file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Class to represent a print book which inherits from Book."""
    
    def __init__(self, title, author, page_count):
        """Initialize print book attributes, including page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class to represent a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []  # List to store book instances

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
