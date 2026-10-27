from books import book_list

def search_book():
    search_id = int(input("Enter the book id to search: "))
    for book in book_list:
        if book["book_id"] == search_id:
            print("Book Found!")
            print("-------------------------")
            print("Book ID:", book["book_id"])
            print("Book Name:", book["book_name"])
            print("Author Name:", book["author_name"])
            print("Book Quantity:", book["book_quantity"])
            return
    print("Book Not Found!")
   
   