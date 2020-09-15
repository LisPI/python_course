from meteoPoint import *


class Meteo(CityObj):
    def __init__(self, address="", phone_number="", meteopoint_list=None):
        super().__init__(address, phone_number)
        if meteopoint_list is None:
            meteopoint_list = []
        self.__meteopoint_list = meteopoint_list

    def add_meteopoint(self, new_meteopoint):
        if isinstance(new_meteopoint, MeteoPoint):
            self.__meteopoint_list.append(new_meteopoint)
            return

    def get_meteopoint_info(self, meteopoint_name):
        for meteopoint in  self.__meteopoint_list:
            if meteopoint_name == meteopoint.get_name():
                return meteopoint.info()
        return "Нет информации для данной метеоточки"

    def info(self):
        return f"Данные о метеоцентре; {super().info()} " \
               f"Количество точек контроля: {len(self.__meteopoint_list)};"
