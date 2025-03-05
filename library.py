import json
import os
from datetime import datetime, timedelta
from book import Book

BOOKS_FILE = "books.json"
FINE_PER_DAY = 10  # Fine amount per day after due date

class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        if not os.path.exists(BOOKS_FILE):
            return []
        with open(BOOKS_FILE, "r") as file:
            return [Book.from_dict(book) for book in json.load(file)]

    def save_books(self):
        with open(BOOKS_FILE, "w") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self, title, author, isbn, genre):
        new_book = Book(title, author, isbn, genre)
        self.books.append(new_book)
        self.save_books()
        return f"Book '{title}' added successfully!"

    def borrow_book(self, isbn, borrower_name):
        for book in self.books:
            if book.isbn == isbn and book.availability:
                book.availability = False
                book.borrower = borrower_name
                book.due_date = datetime.now() + timedelta(days=14)  # 2-week borrowing period
                self.save_books()
                return f"{borrower_name} borrowed '{book.title}'. Due date: {book.due_date.strftime('%Y-%m-%d')}"
        return "Book not available for borrowing."

    def return_book(self, isbn, borrower_name):
        for book in self.books:
            if book.isbn == isbn and book.borrower == borrower_name:
                overdue_days = (datetime.now() - book.due_date).days if book.due_date else 0
                fine = max(0, overdue_days * FINE_PER_DAY)  # Calculate fine if overdue
                book.availability = True
                book.borrower = None
                book.due_date = None
                self.save_books()
                return f"Book returned! Fine: ₹{fine}" if fine else "Book returned successfully!"
        return "Book not found or incorrect borrower."

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.genre.lower()]
