class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books else []

    def member_borrow_book(self, book):
        if book.status == "Available":
            book.Book_borrow_book()
            self.borrowed_books.append(book.title)
            self.member_update_file()
            return f"{self.name} borrowed '{book.title}'."
        return f"Sorry, '{book.title}' is not available."

    def member_return_book(self, book):
        if book.title in self.borrowed_books:
            book.Book_return_book()
            self.borrowed_books.remove(book.title)
            self.member_update_file()
            return f"'{book.title}' is returned by {self.name}."
        return f"'{book.title}' is not borrowed by {self.name}."

    def member_display_info(self):
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {', '.join(self.borrowed_books) if self.borrowed_books else 'None'}"

    def member_save_to_file(self):
        with open("members.txt", "a") as f:
            f.write(f"{self.name},{self.member_id},{','.join(self.borrowed_books)}\n")

    def member_update_file(self):
        members = Member.member_load_members()
        with open("members.txt", "w") as f:
            for member in members:
                if member.member_id == self.member_id:
                    f.write(f"{self.name},{self.member_id},{','.join(self.borrowed_books)}\n")
                else:
                    f.write(f"{member.name},{member.member_id},{','.join(member.borrowed_books)}\n")

    @staticmethod
    def member_load_members():
        members = []
        try:
            with open("members.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    name, member_id = data[0], data[1]
                    borrowed_books = data[2:] if len(data) > 2 else []
                    members.append(Member(name, member_id, borrowed_books))
        except FileNotFoundError:
            pass
        return members
