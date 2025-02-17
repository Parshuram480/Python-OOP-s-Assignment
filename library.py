from book import Book, DigitalBook, book_load_books
from member import Member
from author import Author


class Library:
    def __init__(self):
        self.books = book_load_books()
        self.members = Member.member_load_members()
        self.authors = Author.author_load_authors()

    def library_add_book(self, title, author, isbn, is_digital=False, file_format=None):
        if is_digital:
            book = DigitalBook(title, author, isbn, file_format)
        else:
            book = Book(title, author, isbn)

        self.books.append(book)
        book.book_save_to_file()
        return "Book added successfully!"

    def library_add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        member.member_save_to_file()
        return "Member added successfully!"

    def library_add_author(self, name, books_written=None):
        author = Author(name, books_written)
        self.authors.append(author)
        author.author_save_to_file()
        return "Author added successfully!"

    def library_borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if not member:
            return "Member not found."
        if not book:
            return "Book not found."

        return member.member_borrow_book(book)

    def library_return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if not member:
            return "Member not found."
        if not book:
            return "Book not found."

        return member.member_return_book(book)

    def library_display_books(self):
        return [book.book_display_info() for book in self.books]

    def library_display_members(self):
        return [member.member_display_info() for member in self.members]

    def library_display_authors(self):
        return [author.author_display_info() for author in self.authors]
