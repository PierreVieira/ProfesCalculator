class Transaction:
    def __init__(self, day: int, month: int, year: int, value: float):
        self.__date = {'day': day, 'month': month, 'year': year}
        self.__value = value

    @property
    def date(self):
        return self.__date

    @property
    def value(self):
        return self.__value

    @property
    def period(self):
        return f'{self.date["month"]}/{self.date["year"]}'

    def __str__(self):
        return f'{self.value} | {self.date["day"]}/{self.date["month"]}/{self.date["year"]}'

    def __repr__(self):
        return self.__str__()
