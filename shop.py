from cityObj import *
import pandas as pd


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

    def load_products(self):
        self.__product_list = pd.read_csv('price.csv')

    def show_products(self):
        print(self.__product_list)

    def search_car(self, name, capacity):
        return self.__product_list.query(f"Type == '{name}' and Capacity > {capacity}")
