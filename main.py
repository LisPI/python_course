from city import *
from country import *
import matplotlib.pyplot as plt


def main():
    # shop = Shop("VITALUR", "Lopatina 44", "+34325344", ["bread;1.00", "tea;3.4"])
    # print(shop.info())

    # meteo_point1 = MeteoPoint("meteoPoint1", "Nemiga street", "+3432", {"01": "26", "02": "24", "03": "25"})
    # meteo_point2 = MeteoPoint("meteoPoint2", "Green street", "+3432", {"01": "26", "02": "24"})
    # print(meteo_point1.info())
    # print(meteo_point2.info())

    # meteo = Meteo("Beautiful street", "+374523523")
    # print(meteo.info())

    # rate1 = {"USD": "2.65", "EUR": "3.01"}
    # rate2 = {"USD": "2.66", "EUR": "3.00"}
    # rates = {"03.05": rate1, "04.05": rate2}
    # bank = Bank("Alfa", "Red street", "+35634", 10, "Petrov Ivan", rates)
    # print(bank.info())
    #
    # city = City("LibertyCity", 2000000, "Ivanov", bank=bank, meteo=meteo, shop=shop)
    # print(city.info())

    # print()
    #
    # print(city.info())
    # city.change_population('3')
    #
    # city.change_mayor('папва')
    # city.change_mayor('332fd')
    #
    # city.change_sights('332fd')
    # city.change_sights(['tower', 'stadium'])
    # print(city.info())
    #
    # print()
    #
    # print(bank.info())
    # bank.change_name("BSB", [6, 0, 3, 1])
    # bank.change_name("BNB", [4, 2, 3, 1])
    # print(bank.info())
    # bank.set_rates('14-09-2020')
    # print(bank.info())
    #
    # print()
    #
    # meteo_point2 = MeteoPoint("meteoPoint2", "Green street", "+3432", {"01": "26", "02": "24"})
    # meteo.add_meteopoint(meteo_point2)
    # print(meteo.info())
    # print(meteo.get_meteopoint_info('meteoPoint2'))
    # print(meteo.get_meteopoint_info('mtgfdresgdfggfds'))

    # meteo_salihorsk = MeteoPoint("salihorsk")
    # meteo_gomel = MeteoPoint("gomel")
    # meteo_minsk = MeteoPoint("minsk")
    #
    # meteo.add_meteopoint(meteo_minsk)

    # meteo_test.add_temperature_data('2020-5-15')
    # meteo_test.meteoloader('1', '2019')
    # meteo_test.meteoloader('6', '2020')
    # print(meteo.get_meteopoint_info('minsk'))


    # meteo_gomel.meteoloader('3', '2018')
    # meteo_gomel.meteoloader('8', '2018')
    # meteo.add_meteopoint(meteo_gomel)
    # meteo_grodno = MeteoPoint("grodno")
    # meteo_grodno.meteoloader('7', '2017')
    # meteo.add_meteopoint(meteo_grodno)
    # meteo.meteostatistic()

    bank = Bank("Alfa", "Red street", "+35634", 10, "Petrov Ivan")

    bank.set_rates('12-09-2020')
    bank.set_rates('13-09-2020')
    bank.set_rates('14-09-2020')
    bank.set_rates('15-09-2020')
    bank.set_rates('16-09-2020')
    print(bank.info())
    bank.set_frame_and_series()
    print(bank.get_rates_frame())
    print()
    print(bank.get_eur_series())
    print()
    print(bank.get_rub_series())
    print()
    print(bank.get_usd_series())

    bank.get_rates_frame().plot(kind='bar')
    plt.xlabel("Дата")
    plt.ylabel("Стоимость")
    plt.show()

    meteo = Meteo("Beautiful street", "+374523523")
    print(meteo.info())

    meteo_salihorsk = MeteoPoint("salihorsk")
    meteo_salihorsk.meteoloader('4', '2019')
    meteo.add_meteopoint(meteo_salihorsk)
    meteo.display()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
