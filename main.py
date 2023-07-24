import datetime as dt
from typing import Optional


class Calculator:
    def __init__(self, limit: int):
        self.limit = limit
        self.records = []

    def add_record(self, record: "Record") -> None:
        self.records.append(record)

    def get_today_stats(self) -> int:
        return sum(record.amount for record in self.records if record.date == dt.datetime.now().date())

    def get_week_stats(self) -> int:
        seven_days_ago = dt.datetime.now().date() - dt.timedelta(weeks=1)
        return sum(
            [record.amount for record in self.records if dt.datetime.now().date() >= record.date >= seven_days_ago])


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        today_spent = self.get_today_stats()

        if self.limit > today_spent:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - today_spent} кКал"
        return "Хватит есть!"


class CashCalculator(Calculator):
    USD_RATE = 72.92
    EURO_RATE = 86.58

    def get_today_cash_remained(self, currency: str) -> str:
        currencies = {"rub": ("руб", 1),
                      "usd": ("USD", self.USD_RATE),
                      "eur": ("Euro", self.EURO_RATE)}
        balance = self.limit - self.get_today_stats()
        currency_name, currency_rate = currencies[currency]
        convert_balance = balance / currency_rate

        if convert_balance > 0:
            return f"На сегодня осталось {convert_balance:.2f} {currency_name}"
        elif convert_balance == 0:
            return "Денег нет, держись"
        else:
            return f"Денег нет, держись: твой долг - {abs(convert_balance):.2f} {currency_name}"


class Record:
    def __init__(self, amount: float, comment: str, date: Optional[str] = None):
        self.amount = amount
        if date:
            self.date = dt.date(*map(int, date.split(".")[::-1]))
        else:
            self.date = dt.datetime.now().date()
        self.comment = comment


r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2023")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2023")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2023")
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один", date="24.02.2023")
r5 = Record(amount=84, comment="Йогурт", date="23.02.2023")
r6 = Record(amount=145, comment="Баночка чипсов", date="24.02.2023")

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment="кофе"))
cash_calculator.add_record(Record(amount=300, comment="Серёге на обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2022"))

print(cash_calculator.get_today_cash_remained("rub"))
