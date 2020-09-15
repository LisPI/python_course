from cityObj import *
import requests
import re


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

    def add_temperature_data(self, date):
        response = ''
        if self.__name == "salihorsk":
            response = requests.get(f'https://meteo.by/salihorsk/retro/{date}/').text
        if self.__name == "gomel":
            response = requests.get(f'https://meteo.by/salihorsk/retro/{date}/').text
        if self.__name == "mozyr":
            response = requests.get(f'https://meteo.by/salihorsk/retro/{date}/').text
        if response != '':
            temp = re.findall(r'<td class="temp">день<br /><span><nobr>.+?([+0-9]+).+?</nobr></span></td>', response, re.DOTALL)[0]
            self.__temperature_data[date] = temp

    def info(self):
        return f"Название: {self.__name}; {super().info()} " \
               f"Размер архива метеонаблюдений: {len(self.__temperature_data)}; Архив: {self.__temperature_data}"
