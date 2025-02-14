class Author:
    def __init__(self, name):
        self.name = name
        self.book_written = []

    def add_book(self, book):
        if book.title not in self.book_written:
            self.book_written.append(book.title)

    def display_author_data(self):
        return f"Author: {self.name}, Books Written: {",".join(self.book_written) if self.book_written else "None"}"