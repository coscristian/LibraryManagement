
class FacultyModel:
    def __init__(self, name: str, id: str, building_number: str) -> None:
        self.__name = name
        self.__id = id
        self.__building_number = building_number
        self.__degrees = []

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_degrees(self) -> list:
        return self.__degrees

    def get_building_number(self) -> str:
        return self.__building_number

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_building_number(self, building_number: str):
        self.__building_number = building_number

    def add_degree(self, degree) -> None:
        self.__degrees.append(degree)
