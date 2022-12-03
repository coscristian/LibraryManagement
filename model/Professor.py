from Person import *
from Degree import *

class Professor(Person):
    def __init__(self, num_id: str, name: str, last_name: str, age: str, address: str, phone_number: str) -> None:
        super().__init__(num_id, name, last_name, age, address, phone_number)
        self.__degree = None
        
    def lend_book(self):
        pass
    
    def get_degree(self) -> Degree:
        return self.__degree
    
    def set_degree(self, degree: Degree) -> None:
        self.__degree = degree