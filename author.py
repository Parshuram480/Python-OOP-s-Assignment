class Author:
    def __init__(self, name, books_written=None):
        self.name = name
        self.books_written = books_written if books_written else []

    def author_add_book(self, book_title):
        if book_title not in self.books_written:
            self.books_written.append(book_title)

    def author_display_info(self):
        return f"Author: {self.name}, Books Written: {', '.join(self.books_written) if self.books_written else 'None'}"

    def author_save_to_file(self):
        with open("authors.txt", "a") as f:
            f.write(f"{self.name},{','.join(self.books_written)}\n")