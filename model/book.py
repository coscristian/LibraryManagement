
class BookModel:
    def __init__(self,id: int, title: str, amount: int, amount_available: int, topic: str, author = None) -> None:
        self.__id = id
        self.__title = title
        self.__amount = amount
        self.__amount_available = amount_available
        self.__topic = topic
        self.__professor = None
        self.__student = None
        self.__author = author

    def get_id(self) -> str:
        return self.__id

    def get_title(self) -> str:
        return self.__title

    def get_amount(self) -> int:
        return self.__amount

    def get_amount_available(self) -> int:
        return self.__amount_available

    def get_topic(self) -> str:
        return self.__topic

    def get_professor(self) :
        return self.__professor

    def get_student(self):
        return self.__student

    def get_author(self):
        return self.__author

    def set_amount(self, amount: int) -> None:
        self.__amount = amount

    def set_amount_available(self, amount_available: int) -> None:
        self.__amount = amount_available

    def set_professor(self, professor) -> None:
        self.__professor = professor

    def set_student(self, student) -> None:
        self.__student = student

    def add_author(self, author) -> None:
        self.__author = author
