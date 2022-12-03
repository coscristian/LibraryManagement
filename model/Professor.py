from Person import *

class Professor(Person):
    def __init__(self, num_id: str, name: str, last_name: str, age: str, address: str, phone_number: str) -> None:
        super().__init__(num_id, name, last_name, age, address, phone_number)
    
    def lend_book():
        pass