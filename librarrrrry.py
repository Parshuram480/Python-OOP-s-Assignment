#  Class Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "Available"

    # To display book
    def display_info(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "ISBN": self.isbn,
            "Status": self.status
        }
    
    # function for the borrow book
    def borrowed_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return f"The {self.title} Book is Borrowed."
        else:
            return f"Sorry...The {self.title} Book is Not Available"

    # function for the return book
    def returned_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            return f"The {self.title} Book is Returned and Now Available"
        else:
            return f"The {self.title} Book is already availabe or not borrowed"


# Class for the digital books which inherits the parent class book
class DigitalBook(Book):
    def __init__(self, title, author, isbn, fileFormat):
        super().__init__(title, author, isbn)
        self.fileFormat = fileFormat

    # Display info function which override the perent class method
    def display_info(self):
        info = super().display_info()
        info["File Format"] = self.fileFormat
        return info


# Member Class
class Member:
    def __init__(self, name, memberId):
        self.name = name
        self.memberId = memberId
        self.borrowedBooks = []
        
    # dispaly Member data
    def memberData(self):
        return {
            "Member Name": self.name,
            "Member ID": self.memberId,
            "Book Borrowed": self.borrowedBooks if self.borrowedBooks else "No Books Borrowed."
        }
    
    # Function to boorw book
    def borrow_book(self, book):
        if book.status == "Available":
            book.status = "Borrowed"
            self.borrowedBooks.append({"Title": book.title})
            return f"The {book.title} has been Borrowed by {self.name}"
        else:
            return f"Sorry... The {book.title} Book is not available"

    # Function to return book
    def return_book(self, book):
        for borrowed in self.borrowedBooks:
            if borrowed["Title"] == book.title:
                self.borrowedBooks.remove(borrowed)
                book.status = "Available"
                return f"the {self.name} has return the {book.title}"
        return f"the {self.name} has not Borrowed  the {book.title}"



# Class Author
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def author_books(self, book):
        if book.author == self.name:
            self.books.append(book.title)

    def authorData(self):
        return {
            "Author Name": self.name,
            "Book Written": self.books if self.books else "No books written yet"
        }


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"{book.title} book added successfull in the library."
    
    def display_book(self):
        if len(self.books) == 0:
            return "No Books are available"
        return [book.display_info() for book in self.books]
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.borrowed_book()
        return "book not Found"

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.returned_book()
        return "Book not found"    
        
 
