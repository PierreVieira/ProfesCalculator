import json

from model.transaction import Transaction
from model.transactions import Transactions


class InputManager(object):
    def __init__(self, input_path: str = 'files/input/transactions.json'):
        self.__input_path = input_path

    def __get_periods_json(self):
        with open(self.__input_path) as input_file:
            return json.load(input_file)

    def get_transactions(self) -> Transactions:
        periods_json = self.__get_periods_json()
        data_transactions = []
        for period_json in periods_json:
            month, year = map(int, period_json['period'].split('/'))
            for deposit in period_json['deposits']:
                day = deposit['day']
                value = deposit['value']
                data_transactions.append(Transaction(day=day, month=month, year=year, value=value))
        return Transactions(data=data_transactions)
