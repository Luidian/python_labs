# Необходимо реализовать класс Date, который будет представлять собой дату. Дата должна быть
# представлена тремя полями: год, месяц, день. У данного класса должно быть 3 метода:
# 1. Метод инициализации (__init__);
# 2. Метод для ввода даты с клавиатуры;
# 3. Методы для вывода даты на экран.
from datetime import datetime

class Date:

    def __init__(self, day = datetime.now().day, month = datetime.now().month, year = datetime.now().year):
        self.day = day
        self.month = month
        self.year = year

    def entering_date(self):
        while True:
            print("Enter date in format dd.MM.yyyy")
            date = input()
            valid_date = self.validation(date)
            if valid_date != None:
                return Date(valid_date[0], valid_date[1], valid_date[2])
            
    def print_date(self):
        print(f"{self.day}-{self.month}-{self.year}")
    
    def validation(self, date):
        try:
            date = date.split(".")

            if len(date) != 3:
                print("Oops! This was an invalid date format.")
                return None

            day = int(date[0])
            month = int(date[1])
            year = int(date[2])

            if not (1 <= day <= 31):
                print("Invalid day.")
                return None

            if not(1 <= month <= 12):
                print("Invalid month.")
                return None

            if year < 0:
                print("Invalid year.")
                return None

            return [day, month, year]

        except ValueError:
            print("Oops! This was an invalid date.")
