class Person:
    def __init__(self, id: str, name: str, last_name: str, age: str, address: str, phone_number: str) -> None:
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__address = address
        self.__phone_number = phone_number
        
    def get_id(self) -> str:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_last_name(self) -> str:
        return self.__last_name
    
    def get_age(self) -> str:
        return self.__age
    
    def get_address(self) -> str:
        return self.__address
    
    def get_phone_number(self) -> str:
        return self.__phone_number
                
    def set_age(self, age: str) -> None:
        self.__age = age
        
    def set_address(self, address: str) -> None:
        self.__address = address
        
    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

class Student(Person):
    def __init__(self, id: str, name: str, last_name: str, age: str, address: str, phone_number: str, semester: int) -> None:
        super().__init__(id, name, last_name, age, address, phone_number)
        self.__semester = semester
    
    def get_semester(self) -> int:
        return self.__semester

    def set_semester(self, semester: int) -> None:
        self.__semester = semester
        
    def lend_book() -> None:
        pass
    
    
