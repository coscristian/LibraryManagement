class MandatoryField(Exception):
    def __init__(self, message: str) -> None:
        self.__message = message
    
    def get_message(self) -> str:
        return self.__message
        
    
        