from meteo import *
from shop import *
from bank import *


class City:
    def __init__(self, name="", population_size=0, mayor="", sights=None, bank=Bank(), meteo=Meteo(), shop=Shop()):
        if sights is None:
            sights = []
        self.name = name
        self.population_size = population_size
        self.mayor = mayor
        self.sights = sights
        self.bank = bank
        self.meteo = meteo
        self.shop = shop

    def info(self):
        return f"Город : {self.name}; Численность: {self.population_size}; мэр: {self.mayor}; " \
               f"Число основных достопримечательностей: {len(self.sights)};"
