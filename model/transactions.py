from typing import List

from model.transaction import Transaction


class Transactions:
    def __init__(self, data: List[Transaction]):
        self.__data = data

    @property
    def data(self):
        return self.__data

    def sum_of_deposits(self) -> float:
        return sum(map(lambda transaction: transaction.value, self.data))
