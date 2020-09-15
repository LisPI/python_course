class CityObj:
    def __init__(self, address, phone_number):
        self.__phone_number = phone_number
        self.__address = address

    def info(self):
        return f"Адрес: {self.__address}; Телефон: {self.__phone_number};"
