class Degree:
    def __init__(self, name: str, code_snies: str, total_length_in_semesters: int) -> None:
        self.__name = name
        self.__code_snies = code_snies
        self.__total_length_in_semesters = total_length_in_semesters
        self.__faculty = None
        self.__professors = []
        self.__students = []

    def get_name(self) -> str:
        return self.__name

    def get_code_snies(self) -> str:
        return self.__code_snies

    def get_total_length_in_semesters(self) -> str:
        return self.__total_length_in_semesters

    def get_faculty(self) -> str:
        return self.__faculty

    def get_professors(self) -> list:
        return self.__professors

    def get_students(self) -> list:
        return self.__students

    def set_faculty(self, faculty) -> None:
        self.__faculty = faculty

    def add_professor(self, professor) -> None:
        self.__professors.append(professor)

    def add_student(self, student) -> None:
        self.__students.append(student)
