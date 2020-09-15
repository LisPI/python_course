from meteoPoint import *


class Meteo(CityObj):
    def __init__(self, address="", phone_number="", meteopoint_list=None):
        super().__init__(address, phone_number)
        if meteopoint_list is None:
            meteopoint_list = []
        self.meteopoint_list = meteopoint_list

    def info(self):
        return f"Данные о метеоцентре; {super().info()} " \
               f"Количество точек контроля: {len(self.meteopoint_list)};"
