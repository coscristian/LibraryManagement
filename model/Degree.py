class Degree:
    def __init__(self, name: str, code_snies: str, total_length_in_semesters: int) -> None:
        self.__name = name
        self.__code_snies = code_snies
        self.__total_length_in_semesters = total_length_in_semesters
        
    def get_name(self) -> str:
        return self.__name
    
    def get_code_snies(self) -> str:
        return self.__code_snies
    
    def get_total_length_in_semesters(self) -> str:
        return self.__total_length_in_semesters