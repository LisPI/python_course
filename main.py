class CityObj:
    def __init__(self, address, phone_number):
        self.phone_number = phone_number
        self.address = address

    def info(self):
        return f"Адрес: {self.address}; Телефон: {self.phone_number};"


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


class MeteoPoint(CityObj):
    def __init__(self, name="", address="", phone_number="",
                 temperature_data=None):
        super().__init__(address, phone_number)
        if temperature_data is None:
            temperature_data = {}
        self.name = name
        self.temperature_data = temperature_data

    def info(self):
        return f"Название: {self.name}; {super().info()} " \
               f"Размер архива метеонаблюдений: {len(self.temperature_data)};"


class Meteo(CityObj):
    def __init__(self, address="", phone_number="", meteopoint_list=None):
        super().__init__(address, phone_number)
        if meteopoint_list is None:
            meteopoint_list = []
        self.meteopoint_list = meteopoint_list

    def info(self):
        return f"Данные о метеоцентре; {super().info()} " \
               f"Количество точек контроля: {len(self.meteopoint_list)};"


class Bank(CityObj):
    def __init__(self, name="", address="", phone_number="", board_members=0, head_of_board="", rates=None):
        super().__init__(address, phone_number)
        if rates is None:
            rates = []
        self.name = name
        self.board_members = board_members
        self.head_of_board = head_of_board
        self.rates = rates

    def info(self):
        return f"Наименование банка : {self.name}; {super().info()} " \
               f"Размер архива истории курсов: {len(self.rates)};"


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

    bank.name = "BSB"
    print(city.bank.info())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
