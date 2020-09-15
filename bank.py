from cityObj import *


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
