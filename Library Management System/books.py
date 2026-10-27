
book_list = []
def add_book():
    while True:
        book_id = int(input("Enter the book id: "))
        book_name = input("Enter the book name: ")
        author_name = input("Enter the Author name: ")
        book_quantity = int(input("Enter the book Quantity: "))

        if any(book["book_id"] == book_id for book in book_list):
            print("Book Already Added!")

        else:
            books = {
                "book_id": book_id,
                "book_name": book_name,
                "author_name": author_name,
                "book_quantity": book_quantity
            }

            book_list.append(books)
            print("Book Added Successfully!")

        choice = input("Do you want to add another book? (yes/no): ")

        if choice.lower() != "yes":
            break
def view_books():
    if not book_list:
        print("No Books Found!")
    else:
        print("\n----- Library Books -----")
        for book in book_list:
            print("-------------------------")
            print("Book ID:", book["book_id"])
            print("Book Name:", book["book_name"])
            print("Author Name:", book["author_name"])
            print("Book Quantity:", book["book_quantity"])

