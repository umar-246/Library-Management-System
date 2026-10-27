from books import book_list
from issue import issue_book
def return_book():
    return_id=int(input("Enter the book id to return: "))
    for book in book_list:
        if book["book_id"]==return_id:
            book["book_quantity"]+=1
            print("Book Returned Successfully!")
            print("-------------------------")
            print("Book ID:", book["book_id"])
            print("Book Name:", book["book_name"])
            print("Author Name:", book["author_name"])
            print("Book Quantity:", book["book_quantity"])
            return
        else:
                print("Book Not Available!")
                return