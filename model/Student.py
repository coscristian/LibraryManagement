from Person import *
from Book import *
from Degree import *

class Student(Person):
    def __init__(self, num_id: str, name: str, last_name: str, age: str, address: str, phone_number: str, semester: int) -> None:
        super().__init__(num_id, name, last_name, age, address, phone_number)
        self.__semester = semester
        self.__degree = None
        self.__books = [] 

    def get_degree(self) -> Degree:
        return self.__degree
    
    def get_semester(self) -> int:
        return self.__semester
    
    def get_books(self) -> Book:
        return self.__books
    
    def set_semester(self, semester: int) -> None:
        self.__semester = semester
        
    def set_degree(self, degree: Degree) -> None:
        self.__degree = degree
        
    # set_book()
    def lend_book(self, book: Book) -> None: 
        if len(self.__books) < 2: # Esta validación se debe hacer en el controlador con los datos que vengan de la BBDD
            self.__books.append(book)