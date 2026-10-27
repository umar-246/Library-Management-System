from books import book_list
import datetime
import time
def issue_book():
    issue_id=int(input("Enter the book id to issue: "))
    for book in book_list:
        if book["book_id"]==issue_id:
            if book["book_quantity"]>0:
                book["book_quantity"]-=1
                print("Book Issued Successfully!")
                print("-------------------------")
                print("Book ID:", book["book_id"])
                print("Book Name:", book["book_name"])
                print("Author Name:", book["author_name"])
                print("Book Quantity:", book["book_quantity"])
                print("Issue Date:", datetime.date.today())
                time.sleep(2) 
                return
            else:
                print("Book Not Available!")
                return