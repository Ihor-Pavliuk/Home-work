#Library

#Write a class structure that implements a library. Classes:

#1) Library - name, books = [], authors = []

#2) Book - name, year, author (author must be an instance of Author class)

#3) Author - name, country, birthday, books = []

#Library class

#Methods:

#- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

#- group_by_author(author: Author) - returns a list of all books grouped by the specified author

#- group_by_year(year: int) - returns a list of all the books grouped by the specified year

#All 3 classes must have a readable __repr__ and __str__ methods.

#Also, the book class should have a class variable which holds the amount of all existing books

class Author:

    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name={self.name}, country={self.country}, birthday={self.birthday})"

    def __str__(self):
        return f"{self.name} from {self.country}, born on {self.birthday}"
    

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self,name: str, year: int, author: Author ):
        book = Book[name, year, author]    
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book
    def group_by_author(self, author: Author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        return books
    
    def group_by_year(self, year: int):
        years = []
        for book in self.books:
            if book.year == year:
                years.append(book)
        return years
    def __repr__(self):
        return f"Library(name={self.name}, books={len(self.books)}, authors={len(self.authors)})"

    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books and {len(self.authors)} authors"

class Book:
    total_books = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={self.author.name})"

    def __str__(self):
        return f"'{self.name}' by {self.author.name} ({self.year})"

