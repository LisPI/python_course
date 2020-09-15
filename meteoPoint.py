from cityObj import *


class MeteoPoint(CityObj):
    def __init__(self, name="", address="", phone_number="",
                 temperature_data=None):
        super().__init__(address, phone_number)
        if temperature_data is None:
            temperature_data = {}
        self.__name = name
        self.__temperature_data = temperature_data

    def get_name(self):
        return self.__name

    def add_temperature_data(self):
        pass

    def info(self):
        return f"Название: {self.__name}; {super().info()} " \
               f"Размер архива метеонаблюдений: {len(self.__temperature_data)}; Архив: {self.__temperature_data}"
