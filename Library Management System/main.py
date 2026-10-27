from books import book_list
from books import add_book
from books import view_books
from issue import issue_book
from search import search_book
from return_book  import return_book
from fine import calculate_fine
from report import library_report
def main():
    while True:
        print("\n----- Library Management System -----")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Calculate Fine")
        print("7. Library Report")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            calculate_fine()
        elif choice == "7":
            if not book_list:
                print("No Books Found!")
            else:
                print("\n----- Library Report -----")
                for book in book_list:
                    print("-------------------------")
                    print("Book ID:", book["book_id"])
                    print("Book Name:", book["book_name"])
                    print("Author Name:", book["author_name"])
                    print("Book Quantity:", book["book_quantity"])
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 
    library_report()