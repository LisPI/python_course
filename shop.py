from cityObj import *


class Shop(CityObj):
    def __init__(self, name="", address="", phone_number="", product_list=None):
        super().__init__(address, phone_number)
        if product_list is None:
            product_list = []
        self.__name = name
        self.__product_list = product_list

    def info(self):
        return f"Название: {self.__name}; {super().info()} " \
               f"Количество товаров: {len(self.__product_list)};"
