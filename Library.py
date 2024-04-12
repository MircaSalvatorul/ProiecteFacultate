
import tkinter as tk

# Constante pentru style
BG_COLOR = "#F0F0F0"
BUTTON_COLOR = "#92a128"
TEXT_COLOR = "#333333"
FONT_STYLE = ("Arial", 12)


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        new_book = Book(title, author, genre)
        self.books.append(new_book)
        self.write_to_file()

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                break
        self.write_to_file()

    def display_books(self):
        book_list = []
        for book in self.books:
            book_list.append(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}")
        return book_list

    def write_to_file(self):
        with open("book_list.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.genre}\n")

    def read_from_file(self):
        try:
            with open("book_list.txt", "r") as file:
                for line in file:
                    title, author, genre = line.strip().split(",")
                    self.add_book(title, author, genre)
        except FileNotFoundError:
            pass


def remove_book(title):
    library.remove_book(title)
    display_book()


def show_entries():
    entry_frame.pack(pady=10)
    add_button.config(command=add_and_hide)


def add_and_hide():
    title = title_entry.get()
    author = author_entry.get()
    genre = genre_entry.get()

    library.add_book(title, author, genre)
    entry_frame.pack_forget()
    create_entries()


def create_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)

    entry_frame.pack_forget()
    show_entries()


def display_book():
    for widget in display_frame.winfo_children():
        widget.destroy()

    book_list = library.display_books()
    for book in book_list:
        book_frame = tk.Frame(display_frame, bg=BG_COLOR)
        book_label = tk.Label(book_frame, text=book, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
        book_label.pack(side=tk.LEFT)
        remove_button = tk.Button(book_frame, text="Remove", bg=BUTTON_COLOR, fg="white", font=FONT_STYLE, command=lambda b=book: remove_book(b.split(",")[0].split(": ")[1]))
        remove_button.pack(side=tk.RIGHT)
        book_frame.pack(pady=5, padx=10, fill=tk.X)


# User interface
library = Library()
library.read_from_file()

root = tk.Tk()
root.title("Your own book library")
root.configure(bg=BG_COLOR)


# Read the list of books from a file
with open("book_list.txt", "r") as file:
    books = file.readlines()
    books = [book.strip() for book in books]

# Create a canvas for the left bookshelf
left_bookshelf = tk.Canvas(root, bg="brown", width=300, height=600)
left_bookshelf.pack(side=tk.LEFT)

# Create a canvas for the right bookshelf
right_bookshelf = tk.Canvas(root, bg="brown", width=300, height=600)
right_bookshelf.pack(side=tk.RIGHT)

# Add books to the left bookshelf
for idx, book in enumerate(books[:len(books)//2]):
    left_bookshelf.create_rectangle(10, 10 + idx * 100, 190, 90 + idx * 100, fill="white")
    left_bookshelf.create_text(100, 50 + idx * 100, text=book)

# Add books to the right bookshelf
for idx, book in enumerate(books[len(books)//2:]):
    right_bookshelf.create_rectangle(10, 10 + idx * 100, 190, 90 + idx * 100, fill="white")
    right_bookshelf.create_text(100, 50 + idx * 100, text=book)


# Just Interface stuff to make it pretty
info_label = tk.Label(root, text="What would you like to do today?", font=FONT_STYLE, bg=BG_COLOR, fg=TEXT_COLOR)
info_label.pack(pady=20)

entry_frame = tk.Frame(root, bg=BG_COLOR)

title_entry = tk.Entry(entry_frame, width=30, bg="white", fg=TEXT_COLOR, font=FONT_STYLE)
title_entry.grid(row=0, column=0, padx=5)
title_label = tk.Label(entry_frame, text="Title:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
title_label.grid(row=0, column=1)

author_entry = tk.Entry(entry_frame, width=30, bg="white", fg=TEXT_COLOR, font=FONT_STYLE)
author_entry.grid(row=1, column=0, padx=5)
author_label = tk.Label(entry_frame, text="Author:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
author_label.grid(row=1, column=1)

genre_entry = tk.Entry(entry_frame, width=30, bg="white", fg=TEXT_COLOR, font=FONT_STYLE)
genre_entry.grid(row=2, column=0, padx=5)
genre_label = tk.Label(entry_frame, text="Genre:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_STYLE)
genre_label.grid(row=2, column=1)

add_button = tk.Button(root, text="Add a book to your list", bg=BUTTON_COLOR, fg="white", font=FONT_STYLE, command=show_entries)
add_button.pack(pady=10)

display_frame = tk.Frame(root, bg=BG_COLOR)
display_frame.pack()

display_button = tk.Button(root, text="Display your book list", bg=BUTTON_COLOR, fg="white", font=FONT_STYLE, command=display_book)
display_button.pack(pady=5)

root.mainloop()
