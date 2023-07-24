import datetime as dt


class Calculator:
    def __init__(self, limit: int):
        self.limit = limit
        self.records = []


class CaloriesCalculator(Calculator):
    pass
    # TODO: метод для добавления новой записи о приёме пищи
    # TODO: метод для подсчёта информации о количестве полученных сегодня калорий
    # TODO: метод для определения информации о том, сколько сегодня ещё можно получить калорий
    # TODO: метод для подсчёта информации о количестве полученных калорий за последние семь дней


class CashCalculator(Calculator):
    pass
    # TODO: метод для добавления новой записи о расходах
    # TODO: метод для подсчёта информации о количестве потраченных сегодня денег
    # TODO: метод для определения информации о том, сколько сегодня ещё можно потратить денег (( рубли/доллары/евро ))
    # TODO: метод для подсчёта информации о количестве потраченных денег за последние семь дней


class Record:
    def __init__(self, amount: int, comment: str, date: str = dt.datetime.now().strftime("%d.%m.%Y")):
        self.amount = amount
        self.date = date
        self.comment = comment
