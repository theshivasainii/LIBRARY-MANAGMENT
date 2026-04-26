books = []
issued_books = {}   # store book details

FINE_PER_WEEK = 10   # ₹10 per week late fine

def add_book():
    name = input("Enter book name: ")
    if name in books:
        print("Book already exists")
    else:
        books.append(name)
        print(name, "added successfully")

def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Available books:")
        for b in books:
            print("-", b)

def issue_book():
    import datetime

    book = input("Enter book to issue: ")
    if book in books:
        student = input("Enter student name: ")
        duration = int(input("Enter duration (in days): "))

        issue_date = datetime.date.today()

        issued_books[book] = {
            "student": student,
            "issue_date": issue_date,
            "duration": duration
        }

        books.remove(book)
        print(f"{book} issued to {student} for {duration} days")

    else:
        print("Book not available")

def return_book():
    import datetime

    book = input("Enter book to return: ")

    if book in issued_books:
        today = datetime.date.today()
        data = issued_books[book]

        issue_date = data["issue_date"]
        duration = data["duration"]

        days_used = (today - issue_date).days

        fine = 0
        if days_used > duration:
            extra_days = days_used - duration
            weeks = extra_days // 7 + 1
            fine = weeks * FINE_PER_WEEK

        print("\n--- Return Details ---")
        print("Student:", data["student"])
        print("Days used:", days_used)
        print("Fine:", fine)

        books.append(book)
        del issued_books[book]

        print(book, "returned successfully")

    else:
        print("This book was not issued")

def library():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid input")
            continue

        if choice == 1:
            add_book()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you!")
            break
        else:
            print("Invalid choice")

# Run program
library()