from meteo import *
from shop import *
from bank import *
import re


def error(error_str):
    print('Ошибка: ' + error_str)


class City:
    def __init__(self, name="", population_size=0, mayor="", sights=None, bank=Bank(), meteo=Meteo(), shop=Shop()):
        if sights is None:
            sights = []
        self.__name = name
        self.__population_size = population_size
        self.__mayor = mayor
        self.__sights = sights
        self.__bank = bank
        self.__meteo = meteo
        self.__shop = shop

    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population_size

    def get_sights_size(self):
        return len(self.__sights)

    def change_population(self, new_population_size):
        if isinstance(new_population_size, int):
            self.__population_size = new_population_size
        else:
            error("Численность населения это число")

    def change_mayor(self, new_mayor):
        if re.match(r'[^а-яА-Я]', new_mayor):
            error("Имя мэра должно состоять из букв русского алфавита")
        else:
            self.__mayor = new_mayor

    def change_sights(self, new_sights):
        if isinstance(new_sights, str):
            self.__sights.append(new_sights)
            return
        if isinstance(new_sights, list):
            self.__sights += new_sights
        else:
            error("Неверный формат")

    def info(self):
        return f"Город : {self.__name}; Численность: {self.__population_size}; мэр: {self.__mayor}; " \
               f"Число основных достопримечательностей: {len(self.__sights)};"
