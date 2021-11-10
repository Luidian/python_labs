# Написать функцию, которая принимает 1 аргумент n - целое число и возвращает список первых n чисел Фибоначчи

def fibonacci_num(n):
    sequence = [0, 1]
    if n == 1:
        return [sequence[0]]
    elif n == 2:
        return sequence

    for i in range(n-2):
        a = sequence[i]
        b = sequence[i+1]
        sequence.append(a+b)
    return sequence
