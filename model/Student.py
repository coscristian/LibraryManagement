from Person import *

class Student(Person):
    def __init__(self, num_id: str, name: str, last_name: str, age: str, address: str, phone_number: str, semester: int) -> None:
        super().__init__(num_id, name, last_name, age, address, phone_number)
        self.__semester = semester
    
    def get_semester(self) -> int:
        return self.__semester

    def set_semester(self, semester: int) -> None:
        self.__semester = semester
        
    def lend_book() -> None:
        pass