# Написать функцию, которая принимает 1 аргумент n. n - целое число от 1 до 12. 
# В результате работы функция возвращает время года к которому принадлежит месяц n.
# Пример:
#    Ввод: 3
#    Вывод: весна

def month(num):
    d = {1 : "Зима", 2 : "Зима", 3 : "Весна", 4 : "Весна", 5 : "Весна", 6 : "Лето",
         7 : "Лето", 8 : "Лето", 9 : "Осень", 10 : "Осень", 11 : "Осень", 12 : "Зима"}
    if 1 < num < 12: 
        return "Неверное число"
    return d[num]
