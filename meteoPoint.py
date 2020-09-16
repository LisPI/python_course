from cityObj import *
import requests
import re
import mysql.connector


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
        response = requests.get(f'https://meteo.by/{self.__name}/retro/{date}/').text
        if response.__contains__('Нет данных за выбранный день'):
            print("error old date")
            return
        if response != '':
            temp = re.findall(r'<td class="temp">день<br /><span><nobr>.+?([-+0-9]+)', response, re.DOTALL)[0]
            self.__temperature_data[date] = temp
            return temp

    def meteoloader(self, month, year):
        temp_dict = {}
        for i in range(1, 16):
            temp_dict[f'{year}-{month}-{i}'] = self.add_temperature_data(f'{year}-{month}-{i}')
        self.__insert_to_db(temp_dict)

    def __insert_to_db(self, meteo_data):
        try:
            cnx = mysql.connector.connect(user='root', password='12qwasZX',
                                          host='127.0.0.1',
                                          database='weather')

            cursor = cnx.cursor()
            add_meteodata = ("INSERT INTO meteodata "
                             "(pointname, day_date, temp) "
                             "VALUES (%s, %s, %s)")
            for key in meteo_data:
                meteodata = (self.__name, key, meteo_data[key])
                cursor.execute(add_meteodata, meteodata)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(f"Something is wrong {err}")

    def info(self):
        return f"Название: {self.__name}; {super().info()} " \
               f"Размер архива метеонаблюдений: {len(self.__temperature_data)}; Архив: {self.__temperature_data}"
