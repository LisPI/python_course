from cityObj import *
import requests
import re


def error(error_str):
    print('Ошибка: ' + error_str)


class Bank(CityObj):
    def __init__(self, name="", address="", phone_number="", board_members=0, head_of_board="", rates=None):
        super().__init__(address, phone_number)
        if rates is None:
            rates = {}
        self.__name = name
        self.__board_members = board_members
        self.__head_of_board = head_of_board
        self.__rates = rates

    def change_name(self, new_name, votes):
        if self.__accounting(votes):
            self.__name = new_name

    def set_rates(self, date):
        response = requests.get(f'https://finance.tut.by/arhiv/?date={date}').text
        usd = re.findall(r'currency=USD&date=.+?<td>([0-9.]+)</td>.+?</tr>', response, re.DOTALL)[0]
        eur = re.findall(r'currency=EUR&date=.+?<td>([0-9.]+)</td>.+?</tr>', response, re.DOTALL)[0]
        rub = re.findall(r'currency=RUB&date=.+?<td>([0-9.]+)</td>.+?</tr>', response, re.DOTALL)[0]

        rate = {"USD": usd, "EUR": eur, "RUB": rub}
        self.__rates[date] = rate

    def change_head(self, new_head, votes):
        if self.__accounting(votes):
            self.__head_of_board = new_head

    def info(self):
        return f"Наименование банка : {self.__name}; {super().info()} " \
               f"Размер архива истории курсов: {len(self.__rates)}; Курсы валют: {self.__rates}"

    def __accounting(self, votes):
        votes_count = 0
        for i in votes:
            votes_count += i
        if votes_count != self.__board_members:
            error("Неверное число голосовавших")
            return False
        if votes[0] <= self.__board_members/2:
            error("Нет большинства")
            return False
        return True
