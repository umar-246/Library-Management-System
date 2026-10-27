from books import book_list
from books import add_book
from books import view_books
from search import search_book
def main():
    while True:
        print("\n----- Library Management System -----")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 