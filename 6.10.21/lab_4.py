# Пользователь вводит список произвольной длины. 
# Вывести количество одинаковых элементов. 
# Для ввода списка использовать функцию из 1-го задания.

from lab_1 import enter_list

l = enter_list
l_sort = sorted(l)
element = l_sort[0]
dict = {}
count = 0

for i in l_sort:
    if element == i:
        count += 1
    else:
        dict[element] = count
        count = 1
        element = i
dict[-1] = count + 1 # Добовление последнего слова

for i in dict:
    print(f"Элемент {i} встречается {dict[i]} раз")
