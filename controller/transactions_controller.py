from collections import OrderedDict

from model.transaction import Transaction
from model.transactions import Transactions


class TransactionsController:
    def __init__(self, transactions: Transactions):
        self.__transactions = transactions
        self.__transactions_by_period = self.__get_transactions_by_period(transactions)
        self.__deposits_sum_by_period = self.__get_deposits_sum_by_period(self.__transactions_by_period)

    @staticmethod
    def __dict_is_empty(dict_transactions):
        return not dict_transactions

    @staticmethod
    def __same_months(transaction_one: Transaction, transaction_two: Transaction):
        return transaction_one.date['month'] == transaction_two.date['month']

    def __get_transactions_by_period(self, transactions: Transactions) -> OrderedDict:
        dict_transactions = OrderedDict()
        data_transactions = []
        for transaction in transactions.data:
            if len(data_transactions) > 0:
                last_list_item_transaction = data_transactions[-1]
                if not self.__same_months(transaction, last_list_item_transaction):
                    dict_transactions[last_list_item_transaction.period] = Transactions(data=data_transactions.copy())
                    data_transactions.clear()
            data_transactions.append(transaction)
        if data_transactions:
            dict_transactions[data_transactions[-1].period] = Transactions(data=data_transactions)
        return dict_transactions

    @staticmethod
    def __get_deposits_sum_by_period(transactions_by_period: OrderedDict) -> OrderedDict:
        sum_deposits_by_period = OrderedDict()
        for period, transactions in transactions_by_period.items():
            sum_deposits_by_period[period] = transactions.sum_of_deposits()
        return sum_deposits_by_period

    @property
    def deposits_sum_by_period(self) -> OrderedDict:
        return self.__deposits_sum_by_period

    def get_total_sum(self) -> float:
        sum = 0
        for value in self.__deposits_sum_by_period.values():
            sum += value
        return sum
