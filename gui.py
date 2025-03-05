import tkinter as tk
from tkinter import messagebox

books = {}


def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    genre = genre_entry.get()

    if title and author and isbn and genre:
        books[isbn] = {"Title": title, "Author": author, "Genre": genre, "Borrower": None}
        messagebox.showinfo("Success", f'Book "{title}" added successfully!')
        display_books()
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")

def borrow_book():
    isbn = borrow_isbn_entry.get()
    borrower = borrower_entry.get()

    if isbn in books and books[isbn]["Borrower"] is None:
        books[isbn]["Borrower"] = borrower
        messagebox.showinfo("Success", f'Book "{books[isbn]["Title"]}" borrowed by {borrower}.')
        display_books()
    elif isbn not in books:
        messagebox.showerror("Error", "Book not found.")
    else:
        messagebox.showerror("Error", "Book already borrowed.")

def return_book():
    isbn = return_isbn_entry.get()

    if isbn in books and books[isbn]["Borrower"] is not None:
        books[isbn]["Borrower"] = None
        messagebox.showinfo("Success", f'Book "{books[isbn]["Title"]}" returned.')
        display_books()
    elif isbn not in books:
        messagebox.showerror("Error", "Book not found.")
    else:
        messagebox.showerror("Error", "Book was not borrowed.")

def search_books():
    query = search_entry.get().lower()
    book_list.delete(0, tk.END)

    for isbn, details in books.items():
        if query in details["Title"].lower() or query in details["Author"].lower() or query in isbn:
            book_list.insert(tk.END, f'{details["Title"]} by {details["Author"]} - {isbn}')

def display_books():
    book_list.delete(0, tk.END)
    for isbn, details in books.items():
        status = "Available" if details["Borrower"] is None else f'Borrowed by {details["Borrower"]}'
        book_list.insert(tk.END, f'{details["Title"]} ({details["Genre"]}) by {details["Author"]} - {status}')

root = tk.Tk()
root.title("Library Management System")
root.geometry("600x500")
root.config(bg="#f1faee")


button_style = {"bg": "#e63946", "fg": "white", "font": ("Courier", 10, "bold")}
entry_style = {"bg": "#a8dadc", "fg": "black", "font": ("Courier", 10)}
label_style = {"bg": "#f1faee", "fg": "#457b9d", "font": ("Courier", 10, "bold")}


frame = tk.Frame(root, bg="#f1faee")
frame.pack(pady=10)


tk.Label(frame, text="𝙰𝚍𝚍 𝚊 𝙱𝚘𝚘𝚔", **label_style).grid(row=0, columnspan=2, pady=5)
tk.Label(frame, text="Title:", **label_style).grid(row=1, column=0, sticky="w", padx=5)
title_entry = tk.Entry(frame, **entry_style)
title_entry.grid(row=1, column=1, padx=5)

tk.Label(frame, text="Author:", **label_style).grid(row=2, column=0, sticky="w", padx=5)
author_entry = tk.Entry(frame, **entry_style)
author_entry.grid(row=2, column=1, padx=5)

tk.Label(frame, text="ISBN:", **label_style).grid(row=3, column=0, sticky="w", padx=5)
isbn_entry = tk.Entry(frame, **entry_style)
isbn_entry.grid(row=3, column=1, padx=5)

tk.Label(frame, text="Genre:", **label_style).grid(row=4, column=0, sticky="w", padx=5)
genre_entry = tk.Entry(frame, **entry_style)
genre_entry.grid(row=4, column=1, padx=5)

tk.Button(frame, text="Add Book", command=add_book, **button_style).grid(row=5, columnspan=2, pady=5)


tk.Label(frame, text="𝙱𝚘𝚛𝚛𝚘𝚠 𝚊 𝙱𝚘𝚘𝚔", **label_style).grid(row=6, columnspan=2, pady=5)
tk.Label(frame, text="ISBN:", **label_style).grid(row=7, column=0, sticky="w", padx=5)
borrow_isbn_entry = tk.Entry(frame, **entry_style)
borrow_isbn_entry.grid(row=7, column=1, padx=5)

tk.Label(frame, text="Borrower:", **label_style).grid(row=8, column=0, sticky="w", padx=5)
borrower_entry = tk.Entry(frame, **entry_style)
borrower_entry.grid(row=8, column=1, padx=5)

tk.Button(frame, text="Borrow Book", command=borrow_book, **button_style).grid(row=9, columnspan=2, pady=5)


tk.Label(frame, text="𝚁𝚎𝚝𝚞𝚛𝚗 𝚊 𝙱𝚘𝚘𝚔", **label_style).grid(row=10, columnspan=2, pady=5)
tk.Label(frame, text="ISBN:", **label_style).grid(row=11, column=0, sticky="w", padx=5)
return_isbn_entry = tk.Entry(frame, **entry_style)
return_isbn_entry.grid(row=11, column=1, padx=5)

tk.Button(frame, text="Return Book", command=return_book, **button_style).grid(row=12, columnspan=2, pady=5)


tk.Label(frame, text="𝚂𝚎𝚊𝚛𝚌𝚑 𝙱𝚘𝚘𝚔𝚜", **label_style).grid(row=13, columnspan=2, pady=5)
tk.Label(frame, text="Search:", **label_style).grid(row=14, column=0, sticky="w", padx=5)
search_entry = tk.Entry(frame, **entry_style)
search_entry.grid(row=14, column=1, padx=5)

tk.Button(frame, text="Search", command=search_books, **button_style).grid(row=15, columnspan=2, pady=5)


book_list = tk.Listbox(root, width=80, bg="#1d3557", fg="white", font=("Courier", 10))
book_list.pack(pady=10)

display_books()
root.mainloop()
