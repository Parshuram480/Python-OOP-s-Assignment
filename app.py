from library import Library

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Add Author")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Display Books")
        print("7. Display Members")
        print("8. Display Authors")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            is_digital = input("Is it a digital book? (yes/no): ").strip().lower() == "yes"

            if is_digital:
                file_format = input("Enter file format (pdf/EPub/Word): ")
                print(library.library_add_book(title, author, isbn, is_digital=True, file_format=file_format))
            else:
                print(library.library_add_book(title, author, isbn))

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            print(library.library_add_member(name, member_id))

        elif choice == "3":
            name = input("Enter author name: ")
            books_written = input("Enter books written by the author (comma-separated): ").split(",")
            books_written = [book.strip() for book in books_written if book.strip()]
            print(library.library_add_author(name, books_written))

        elif choice == "4":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title to borrow: ")
            print(library.library_borrow_book(member_name, book_title))

        elif choice == "5":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title to return: ")
            print(library.library_return_book(member_name, book_title))

        elif choice == "6":
            print("\nBooks in Library:")
            for book in library.library_display_books():
                print(book)

        elif choice == "7":
            print("\nLibrary Members:")
            for member in library.library_display_members():
                print(member)

        elif choice == "8":
            print("\nAuthors:")
            for author in library.library_display_authors():
                print(author)

        elif choice == "9":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

main()