# Task 2 Library
class Library:
    def __init__(self, name: str):
        self.name = name
        self.available_books = list()
        self.authors = list()

    def __repr__(self) -> str:
        return f"Library:{self.name}, {self.available_books}, {self.authors}"

    def __str__(self) -> str:
        return f" {self.name} library with , books - {self.available_books}, written by -  {self.authors}"

    def new_book(self, name: str, year: int, author: str):
        n_book = Book(name, year, author)
        self.available_books.append(n_book)
        self.authors.append(n_book.author)
        Book.total_books += 1
        return n_book

    def group_by_author(self, author: str):
        query = author
        if query == self.authors:
            print(self.available_books)

    def group_by_author1(self, author: str):
        return [b for b in self.available_books if b.author == author]

    def group_by_year(self, year: int):
        return [b for b in self.available_books if b.year == year]


class Book:
    total_books = 0

    def __init__(self, name: str, year: int, author):
        self.name = name
        self.year = year
        self.author = Author

    def __repr__(self) -> str:
        return f"Book: {self.name}, {self.year}, by {self.author}"

    def __str__(self) -> str:
        return f"Name: {self.name}"


class Author:
    def __init__(self, name: str, country: str, birthday: int):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.available_books = list()

    def add_book(self, book_name: str):
        self.available_books.append(book_name)

    def __repr__(self) -> str:
        return f"Book: {self.name}, {self.country}, {self.birthday}, {self.available_books}"

    def __str__(self) -> str:
        return f"Book: {self.name}, from {self.country}, born on {self.birthday}, wrote {self.available_books}"


#b1 = Book(name="Arch of Triumph", year=1945, author="Erich Maria Remarque")
#b2 = Book(name="All Quiet on the Western Front", year=1929, author="Erich Maria Remarque")
#b3 = Book(name="Road of Pain", year=1990, author="Vasyl Stus")



