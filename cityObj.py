class CityObj:
    def __init__(self, address, phone_number):
        self.phone_number = phone_number
        self.address = address

    def info(self):
        return f"Адрес: {self.address}; Телефон: {self.phone_number};"
