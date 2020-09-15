from cityObj import *


class Shop(CityObj):
    def __init__(self, name="", address="", phone_number="", product_list=None):
        super().__init__(address, phone_number)
        if product_list is None:
            product_list = []
        self.name = name
        self.product_list = product_list

    def info(self):
        return f"Название: {self.name}; {super().info()} " \
               f"Количество товаров: {len(self.product_list)};"
