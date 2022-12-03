from Book import *

class Topic:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__books = [] 
        
    def get_name(self) -> None:
        return self.__name
    
    def get_books(self) -> Book:
        return self.__books
    
    def add_book(self, book: Book) -> None:
        self.__books.append(book)