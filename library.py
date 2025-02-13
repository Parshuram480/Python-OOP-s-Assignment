class Book:
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def bookDetails(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "ISBN": self.isbn,
            "Status": self.status
        }

    
class Member:
    def __init__(self, name, memberId):
        self.name = name
        self.memberId = memberId
        self.borrowedBooks = []

    def memeberData(self,):
        return {
            "Member Name": self.name,
            "Member ID": self.memberId,
            "Book Borrowed": self.borrowedBooks
        }


# Class Author
class Author:
    def __init__(self, name, booksWritten):
        self.name = name
        self.books = booksWritten

    def authorData(self):
        return {
            "Author Name": self.name,
            "Book Written": self.books
        }


class Library:
    def __init__(self):
        pass


class DigitalBook(Book):
    def __init__(self, title, author, isbn, status, fileFormate):
        super().__init__(title, author, isbn, status)
        self.fileFormate = fileFormate


m1 = Member("Ajit", 14413244, "YES")
print(m1.memeberData())