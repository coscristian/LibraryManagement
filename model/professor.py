from model.person import PersonModel

class ProfessorModel(PersonModel):
    def __init__(self, num_id: str, name: str, last_name: str, age: str, address: str, phone_number: str, degree = None, books = [] ) -> None:
        super().__init__(num_id, name, last_name, age, address, phone_number)
        self.__degree = degree
        self.__books = books

    def get_degree(self):
        return self.__degree

    def get_books(self):
        return self.__books

    def set_degree(self, degree) -> None:
        self.__degree = degree

    # set_book()
    def lend_book(self, book) -> None:
        if len(self.__books) < 2:  # Esta validación se debe hacer en el controlador con los datos que vengan de la BBDD
            self.__books.append(book)
