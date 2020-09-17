from cityObj import *
import requests
import re
import pandas as pd


class Country:
    def __init__(self, name="", cities=None):
        if cities is None:
            cities = []
        self.__name = name
        self.__cities_obj = cities

    def info(self):
        return f"Наименование страны : {self.__name}; Города: {len(self.__cities_obj)}"

    def pre_statistics(self):
        name = (o.get_name() for o in self.__cities_obj)
        self.__cities = pd.Series(name)

        population = (o.get_population() for o in self.__cities_obj)
        self.__population = pd.Series(population)

        sights_size = (o.get_sights_size() for o in self.__cities_obj)
        self.__sights_size = pd.Series(sights_size)

        self.__country_df = self.__cities.to_frame("city")
        self.__country_df["population"] = self.__population
        self.__country_df["sights"] = self.__sights_size

    def people_stat(self, amount=None):
        if amount is None:
            return self.__country_df[['city', 'population']]
        return self.__country_df[self.__country_df['population'] > amount]['city']

    def sight_stat(self, amount=None):
        if amount is None:
            return self.__country_df[self.__country_df['sights'] == 0]['city']
        return self.__country_df[self.__country_df['sights'] < amount]['city']
