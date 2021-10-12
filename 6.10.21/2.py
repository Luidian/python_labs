# Написать функцию, которая принимает 1 аргумент n. n - целое число от 1 до 12. 
# В результате работы функция возвращает время года к которому принадлежит месяц n.
# Пример:
#    Ввод: 3
#    Вывод: весна

def month(num):
    d = {"Зима" : [12, 1, 2], "Весна" : [3, 4, 5], "Лето" : [6, 7, 8], "Осень" : [9, 10, 11]}
    if num < 1 and num > 12: 
        return "Неверное число"
    for i in d:
        if num in d[i]:
            return i


print(month(3))