# Необходимо реализовать класс Date, который будет представлять собой дату. Дата должна быть
# представлена тремя полями: год, месяц, день. У данного класса должно быть 3 метода:
# 1. Метод инициализации (__init__);
# 2. Метод для ввода даты с клавиатуры;
# 3. Методы для вывода даты на экран.

class Date:
    
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def entering_date(self):
        print("Enter date in format dd.MM.yyyy")
        date = input().split(".")
        self.__init__(date[0], date[1], date[2])

    def print_date(self):
        print(f"{self._day}:{self._month};{self._year}")

    def day(self):
        return self._day
        
    def month(self):
        return self._month
    
    def year(self):
        return self._year
