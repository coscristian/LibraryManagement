from model.employee import EmployeeModel

class LibraryEmployeeModel(EmployeeModel):
    def __init__(self, num_id: str, name: str, last_name: str, age: str, address: str, phone_number: str, salary: float,
                 is_admin: bool) -> None:
        super().__init__(num_id, name, last_name, age, address, phone_number, salary)
        self.__is_admin = is_admin

    def get_is_admin(self) -> bool:
        return self.__is_admin

    def set_is_admin(self, is_admin: bool) -> None:
        self.__is_admin = is_admin

    def give_book_back(self):
        pass
