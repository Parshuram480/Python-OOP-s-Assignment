# Member Class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    # Function to boorw book
    def borrow_book(self, book):
        if book.status == "Available":
            book.borrowed_book()
            self.borrowed_books.append(book.title)
            return f"{self.name} borrowed {book.title}"
        return f"sorry, {book.title} not available." 

    # Function to return book
    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.returned_book()
            self.borrowed_books.remove(book.title)
            return f"{book.title} is returned by {self.name}"
        return f"{book.title} is not borrowed by {self.name}"
        
    # dispaly Member data
    def display_member_data(self):
        return f"Member: {self.name}, Member ID: {self.member_id}, Borrowed Books: {",".join(self.borrowed_books) if self.borrowed_books else 'None'}"
        

