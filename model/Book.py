class Book:
    def __init__(self, id: str, title: str, amount: int, amount_available: int, topic: str) -> None:
        self.__id = id
        self.__title = title
        self.__amount = amount
        self.__amount_available = amount_available
        self.__topic = topic
        
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
    
    def set_amount(self, amount: int) -> None:
        self.__amount = amount
        
    def set_amount_available(self, amount_available: int) -> None:
        self.__amount = amount_available
    
    