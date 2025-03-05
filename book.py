import json
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, genre, availability=True, borrower=None, due_date=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability
        self.borrower = borrower  
        self.due_date = due_date  
    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'genre': self.genre,
            'availability': self.availability,
            'borrower': self.borrower,
            'due_date': self.due_date.strftime('%Y-%m-%d') if self.due_date else None
        }

    @staticmethod
    def from_dict(data):
        return Book(
            title=data['title'],
            author=data['author'],
            isbn=data['isbn'],
            genre=data['genre'],
            availability=data['availability'],
            borrower=data.get('borrower'),
            due_date=datetime.strptime(data['due_date'], '%Y-%m-%d') if data.get('due_date') else None
        )
