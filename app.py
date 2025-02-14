from book import Book, DigitalBook
from member import Member
from library import Library

library = Library()

while True:
    print()
    print("1. Add book")
    print("2. Add Member")
    print("3. Borrow book")
    print("4. Retturn book")
    print("5. Display book")
    print("6. Display members")
    print("7. Exit")

    num = int(input("Enter The Number: "))

    if num == 1:
        title = input("Enter the Book title: ")
        author = input("Enter the Book Auhror name: ")
        isbn = int(input("Enter the Book ISBN no: "))
        format = input("is it the digital Book ? (yes/no): ").lower()
        if format == "yes":
            file_format = input("Enter the Book Formate (pdf/word): ")
            book = DigitalBook(title, author, isbn, file_format)
        else:
            book = Book(title, author, isbn)
        print(library.add_book(book))

    elif num == 2:
        name = input("Enter the Member Name: ")
        member_id = int(input("Enter the MEmber ID: "))
        member = Member(name, member_id)
        print(library.add_member(member))

    elif num == 3:
        member_name = input("Enter the Member Name: ")
        book_name = input("Enter The Book Name: ")
        print(library.borrow_book(member_name, book_name))

    elif num == 4:
        member_name = input("Enter the Member Name: ")
        book_name = input("Enter The Book Name: ")
        print(library.return_book(member_name, book_name))

    elif num == 5:
        print("\nBooks:")
        print("\n".join(library.display_books()))

    elif num == 6:
        print("\nMembers:")
        print("\n".join(library.display_members()))
    
    elif num == 7:
        break
        
    else:
        print("You have entered Invalid Number!, Please Enter the Valid Number.")

