import datetime as dt
from abc import ABC, abstractmethod

DATE_FORMAT = "%d.%m.%Y"
USD_RATE = 90.38
EURO_RATE = 100.66


class Calculator(ABC):
    def __init__(self, limit: int):
        self.limit = limit
        self.records = []

    def add_record(self, record: "Record") -> None:
        self.records.append(record)

    def get_today_stats(self) -> int:
        return sum(record.amount for record in self.records)

    @abstractmethod
    def get_week_stats(self) -> str:
        pass


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        today_spent = sum(record.amount for record in self.records if record.date == dt.datetime.now().date())

        if self.limit > today_spent:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - today_spent} кКал"
        else:
            return "Хватит есть!"

    def get_week_stats(self, currency: str) -> str:
        seven_days_ago = dt.datetime.now().date() - dt.timedelta(days=7)
        week_spent = sum([record.amount for record in self.records if record.date > seven_days_ago])
        return f"За последние семь дней вы получили {week_spent} кКал"


class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency: str) -> str:
        today_spent = sum(record.amount for record in self.records if record.date == dt.datetime.now().date())

        if currency == "rub":
            currency = "руб"
            self.current_limit = self.limit
        elif currency == "usd":
            currency = "USD"
            self.current_limit = self.limit / USD_RATE
            today_spent = today_spent / USD_RATE
        else:
            currency = "Euro"
            self.current_limit = self.limit / EURO_RATE
            today_spent = today_spent / EURO_RATE

        if self.limit > today_spent:
            return f"На сегодня осталось {self.current_limit - today_spent:.2f} {currency}"
        elif self.limit == today_spent:
            return "Денег нет, держись"
        else:
            return f"Денег нет, держись: твой долг - {today_spent - self.current_limit} {currency}"

    def get_week_stats(self, currency: str) -> str:
        seven_days_ago = dt.datetime.now().date() - dt.timedelta(days=7)
        week_spent = sum([record.amount for record in self.records if record.date > seven_days_ago])

        if currency == "руб":
            return f"За последние семь дней вы потратили {week_spent:.2f} {currency}"
        elif currency == "usd":
            return f"За последние семь дней вы потратили {week_spent / USD_RATE:.2f} {currency}"
        else:
            return f"За последние семь дней вы потратили {week_spent / EURO_RATE:.2f} {currency}"


class Record:
    def __init__(self, amount: float, comment: str, date: str = dt.datetime.now().strftime(DATE_FORMAT)):
        self.amount = amount
        self.date = dt.date(*map(int, date.split(".")[::-1]))
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
