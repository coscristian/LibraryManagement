from model.person import PersonModel

class EmployeeModel(PersonModel):
    def __init__(self, num_id: str, name: str, last_name: str, age: str, address: str, phone_number: str,
                 salary: float) -> None:
        super().__init__(num_id, name, last_name, age, address, phone_number)
        self.__salary = salary

    def get_salary(self) -> float:
        return self.__salary

    def set_salary(self, salary: float) -> None:
        self.__salary = salary
