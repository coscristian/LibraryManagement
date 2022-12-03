from Book import *

class Author:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__books = [] 
        
    def get_name(self) -> str:
        return self.__name
    
    def get_books(self) -> Book:
        return self.__books
    
    def add_book(self, book: Book) -> None:
        self.__books.append(book)