class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "Available"

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

    # To display book
    def display_info(self):
        return f"Title:{self.title}, Author:{self.author}, ISBN:{self.isbn}, Status:{self.status}"


 
# Class for the digital books which inherits the parent class book
class DigitalBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    # Display info function which override the perent class method
    def display_info(self):
        info = super().display_info()
        return f"{info}, File Format: {self.file_format}"
