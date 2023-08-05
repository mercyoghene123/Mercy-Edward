import datetime

class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower_id = None
        self.borrow_date = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        genres = {}

        for book in self.books:
            if book.genre not in genres:
                genres[book.genre] = []
            genres[book.genre].append(book)

        for genre, books in genres.items():
            print(f"\nGenre: {genre}")
            for book in books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, "
                      f"Borrowed: {'Yes' if book.is_borrowed else 'No'}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Book found - Title: {book.title}, Author: {book.author}, "
                      f"Genre: {book.genre}, ISBN: {book.isbn}, Borrowed: {'Yes' if book.is_borrowed else 'No'}")
                return
        print("Book not found.")

    def borrow_book(self, title, borrower_id):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrower_id = borrower_id
                    book.borrow_date = datetime.date.today()
                    print(f"Book '{book.title}' has been borrowed by {borrower_id}.")
                    return
                else:
                    print(f"Book '{book.title}' is already borrowed.")
                    return
        print("Book not found.")

    def borrowed_books(self):
        borrowed_books_list = []
        for book in self.books:
            if book.is_borrowed:
                borrowed_books_list.append(book)
        return borrowed_books_list


def main():
    library = Library()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. View Borrowed Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, genre, isbn)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == '2':
            print("\nList of Books categorized by Genre:")
            library.view_books()

        elif choice == '3':
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == '4':
            title = input("Enter book title to borrow: ")
            borrower_id = input("Enter your ID: ")
            library.borrow_book(title, borrower_id)

        elif choice == '5':
            print("\nBorrowed Books:")
            borrowed_books = library.borrowed_books()
            for book in borrowed_books:
                print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, "
                      f"ISBN: {book.isbn}, Borrower ID: {book.borrower_id}, Borrow Date: {book.borrow_date}")

        elif choice == '6':
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
