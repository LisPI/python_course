from cityObj import *


class MeteoPoint(CityObj):
    def __init__(self, name="", address="", phone_number="",
                 temperature_data=None):
        super().__init__(address, phone_number)
        if temperature_data is None:
            temperature_data = {}
        self.name = name
        self.temperature_data = temperature_data

    def info(self):
        return f"Название: {self.name}; {super().info()} " \
               f"Размер архива метеонаблюдений: {len(self.temperature_data)};"
