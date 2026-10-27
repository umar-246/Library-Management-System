
from books import book_list

def library_report():

    total_books = len(book_list)

    total_available = 0
    total_issued = 0

    for book in book_list:
        total_available += book["book_quantity"]

    total_issued = 0 
    print("\n----- Library Report -----")
    print("Total Registered Books:", total_books)
    print("Total Available Copies:", total_available)
    print("Total Issued Copies:", total_issued)
