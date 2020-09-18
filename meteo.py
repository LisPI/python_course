from meteoPoint import *
import pandas as pd
import matplotlib.pyplot as plt


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

    def meteostatistic(self):
        try:
            cnx = mysql.connector.connect(user='root', password='12qwasZX',
                                          host='127.0.0.1',
                                          database='weather')

            print('Общая статистика')
            print('{:<30s}|{:<20s}|{:<20s}|{:<20s}'.format('Параметр', 'Значение', 'Дата', 'Имя точки'))

            cursor = cnx.cursor()
            query = ("select temp, day_date, pointname FROM meteodata WHERE temp = (SELECT MIN(temp) FROM meteodata GROUP BY pointname LIMIT 1) LIMIT 1")
            cursor.execute(query)
            min = cursor.fetchone()

            print('{:<30s}|{:^20d}|{:^20s}|{:^20s}'.format('Минимальная температура', min[0], min[1], min[2]))

            query = ("select temp, day_date, pointname FROM meteodata WHERE temp = (SELECT MAX(temp) FROM meteodata GROUP BY pointname LIMIT 1) LIMIT 1")
            cursor.execute(query)
            max = cursor.fetchone()

            print('{:<30s}|{:^20d}|{:^20s}|{:^20s}'.format('Максимальная температура', max[0], max[1], max[2]))

            query = ("select avg(temp) FROM meteodata")
            cursor.execute(query)
            average = cursor.fetchone()
            print('{:<30s}|{:^20f}|{:^20s}|{:^20s}'.format('Средняя температура', average[0], '-', '-'))

            print()
            print('Статистика по точкам')
            print('{:<30s}|{:<20s}|{:<20s}|{:<20s}'.format('Параметр', 'Значение', 'Дата', 'Имя точки'))
            for point in self.__meteopoint_list:
                query = ("select temp, day_date, pointname FROM meteodata WHERE pointname = %s AND temp = (SELECT MIN(temp) FROM meteodata WHERE pointname = %s LIMIT 1) LIMIT 1")
                cursor.execute(query, (point.get_name(), point.get_name()))
                minpointdata = cursor.fetchone()
                print('{:<30s}|{:^20d}|{:^20s}|{:^20s}'.format('Минимальная температура', minpointdata[0], minpointdata[1], minpointdata[2]))

                query = ("select temp, day_date, pointname FROM meteodata WHERE pointname = %s AND temp = (SELECT MAX(temp) FROM meteodata WHERE pointname = %s LIMIT 1) LIMIT 1")
                cursor.execute(query, (point.get_name(), point.get_name()))
                maxpointdate = cursor.fetchone()
                print('{:<30s}|{:^20d}|{:^20s}|{:^20s}'.format('Максимальная температура', maxpointdate[0], maxpointdate[1], maxpointdate[2]))

            print()
            print('Характеристика данных')
            print('{:<30s}|{:<20s}'.format('Параметр', 'Значение'))

            query = ("SELECT COUNT(distinct pointname) FROM meteodata")
            cursor.execute(query)
            countpoints = cursor.fetchone()[0]
            print('{:<30s}|{:<20d}'.format('количество точек', countpoints))

            query = ("SELECT COUNT(1) FROM meteodata")
            cursor.execute(query)
            countpoints = cursor.fetchone()[0]
            print('{:<30s}|{:<20d}'.format('количество записей', countpoints))

            query = ("SELECT COUNT(1) FROM meteodata WHERE temp > 0")
            cursor.execute(query)
            countpoints = cursor.fetchone()[0]
            print('{:<30s}|{:<20d}'.format('число дней с T>0', countpoints))

            query = ("SELECT COUNT(1) FROM meteodata WHERE temp < 0")
            cursor.execute(query)
            countpoints = cursor.fetchone()[0]
            print('{:<30s}|{:<20d}'.format('число дней с T<0', countpoints))

            query = ("SELECT COUNT(1) FROM meteodata WHERE temp = 0")
            cursor.execute(query)
            countpoints = cursor.fetchone()[0]
            print('{:<30s}|{:<20d}'.format('число дней с T=0', countpoints))

            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(f"Something is wrong {err}")

    def display(self):
        cnx = mysql.connector.connect(user='root', password='12qwasZX',
                                      host='127.0.0.1',
                                      database='weather')

        df = pd.read_sql('select pointname, count(*) as count FROM meteodata GROUP BY pointname', cnx)
        print(df)
        series = pd.Series(data=df['count'].to_list(), index=df['pointname'].to_list())
        series.plot(kind='bar')
        plt.show()
