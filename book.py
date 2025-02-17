class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def book_borrow_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
            self.book_update_file()
            return f"the book {self.title} is borrowed."
        return f"Sorry, the book {self.title} is not available."

    def book_return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            self.book_update_file()
            return f"The book {self.title} is returned and now available."
        return f"The book {self.title} is already available or not borrowed."

    def book_display_info(self):
        return f"Title:{self.title}, Author:{self.author}, ISBN:{self.isbn}, Status:{self.status}"

    def book_save_to_file(self):
        with open("books.txt", "a") as f:
            f.write(f"{self.title},{self.author},{self.isbn},{self.status}\n")

    def book_update_file(self):
        books = book_load_books()
        with open("books.txt", "w") as f:
            for book in books:
                if book.isbn == self.isbn:
                    f.write(f"{self.title},{self.author},{self.isbn},{self.status}\n")
                else:
                    f.write(f"{book.title},{book.author},{book.isbn},{book.status}\n")


# digigital book class which inherits the Book class
class DigitalBook(Book):
    def __init__(self, title, author, isbn, file_format, status="Available"):
        super().__init__(title, author, isbn, status)
        self.file_format = file_format

    def book_display_info(self):
        return f"{super().book_display_info()}, File Format: {self.file_format}"

    def book_save_to_file(self):
        with open("books.txt", "a") as f:
            f.write(f"{self.title},{self.author},{self.isbn},{self.status},{self.file_format}\n")

    def book_update_file(self):
        books = book_load_books()
        with open("books.txt", "w") as f:
            for book in books:
                if book.isbn == self.isbn:
                    f.write(f"{self.title},{self.author},{self.isbn},{self.status},{self.file_format}\n")
                else:
                    if isinstance(book, DigitalBook):
                        f.write(f"{book.title},{book.author},{book.isbn},{book.status},{book.file_format}\n")
                    else:
                        f.write(f"{book.title},{book.author},{book.isbn},{book.status}\n")

# load the to read the file
def book_load_books():
    books = []
    try:
        with open("books.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 5:
                    book = DigitalBook(data[0], data[1], data[2], data[4], data[3])
                else:
                    book = Book(data[0], data[1], data[2], data[3])
                books.append(book)
    except FileNotFoundError:
        pass
    return books
