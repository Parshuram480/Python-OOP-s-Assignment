import os
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()
        return f"Book {book.title} added Succefully"
    
    def add_member(self, member):
        self.members.append(member)
        self.save_data()
        return f"Member {member.name} added succussfully."
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None 
    
    def borrow_book(self, name, title):
        member = self.find_member(name)
        book = self.find_book(title)

        if book and member:
            result = member.borrow_book(book)
            self.save_data()
            return result
        return "Books or Member not found"
    
    def return_book(self, name, title):
        member = self.find_member(name)
        book = self.find_book(title)

        if book and member:
            result = member.return_book(book)
            self.save_data()
            return result
        return "Book or Member not found."
    
    def display_books(self):
        return [book.display_info() for book in self.books]
    
    def display_members(self):
        return [member.display_member_data() for member in self.members]
    
    def save_data(self):
        f = open("library_data.txt", "w")
        for book in self.books:
            f.write(f"Book, {book.title}, {book.author}, {book.isbn}, {book.status}\n")
        
        for member in self.members:
            f.write(f"Member, {member.name}, {member.member_id}, {",".join(member.borrowed_books)}\n")

    def load_data(self):
        if os.path.exists("library_data.txt"):
            f =  open("library_data.txt", "r")
            for line in f:
                data = line.strip().split(",")
                if data[0] == "Book":
                    self.books.append(Book(data[1], data[2], data[3]))
                elif data[0] == "Member":
                    member = Member(data[1], data[2])
                    member.borrowed_books = data[3:]
                    self.members.append(member)
        