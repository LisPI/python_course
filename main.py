from city import *


def main():
    shop = Shop("VITALUR", "Lopatina 44", "+34325344", ["bread;1.00", "tea;3.4"])
    print(shop.info())

    meteo_point1 = MeteoPoint("meteoPoint1", "Nemiga street", "+3432", {"01": "26", "02": "24", "03": "25"})
    meteo_point2 = MeteoPoint("meteoPoint2", "Green street", "+3432", {"01": "26", "02": "24"})
    print(meteo_point1.info())
    print(meteo_point2.info())

    meteo = Meteo("Beautiful street", "+374523523", [meteo_point1, meteo_point2])
    print(meteo.info())
    print(meteo.meteopoint_list[1].info())

    rate1 = {"USD": "2.65", "EUR": "3.01"}
    rate2 = {"USD": "2.66", "EUR": "3.00"}
    rates = {"03.05": rate1, "04.05": rate2}
    bank = Bank("Alfa", "Red street", "+35634", 12, "Petrov Ivan", rates)
    print(bank.info())

    city = City("LibertyCity", 2000000, "Ivanov", bank=bank, meteo=meteo, shop=shop)
    print(city.info())

    city.change_population('3')

    city.change_mayor('папва')
    city.change_mayor('332fd')

    city.change_sights('332fd')
    city.change_sights(['tower', 'stadium'])
    print(city.info())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
