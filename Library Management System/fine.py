
from books import book_list
import datetime


def calculate_fine():
    try:
        book_id = int(input("Enter the book ID to calculate fine: "))

        for book in book_list:
            if book["book_id"] == book_id:

                issue_date = input("Enter the issue date (YYYY-MM-DD): ")
                return_date = input("Enter the return date (YYYY-MM-DD): ")

                issue_date = datetime.datetime.strptime(
                    issue_date, "%Y-%m-%d"
                ).date()

                return_date = datetime.datetime.strptime(
                    return_date, "%Y-%m-%d"
                ).date()

                if return_date < issue_date:
                    print("Return date cannot be before issue date!")
                    return

                days_borrowed = (return_date - issue_date).days

                print("Days Borrowed:", days_borrowed)

                if days_borrowed > 14:
                    fine_amount = (days_borrowed - 14) * 5
                    print("Fine Amount: Rs.", fine_amount)
                else:
                    print("No Fine. Book returned on time.")

                return

        print("Book Not Found!")

    except ValueError:
        print("Invalid input! Enter a valid book ID and date.")


if __name__ == "__main__":
    calculate_fine()
