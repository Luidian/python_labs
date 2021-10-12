# Написать функцию, которая принимает 1 аргумент n - целое число и выводит первые n чисел Фибоначчи

def fibonacci_num(n):
    a = 0
    b = 1
    if n > 0:
        print(a)
        if n > 1:
            print(b)
            if n > 2:
                for i in range(n-2):
                    print(a+b)
                    temp = a
                    a = b
                    b += temp

fibonacci_num(5)