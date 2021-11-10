# Написать функцию, которая принимает 1 аргумент - целое число и возвращает True, если число простое и False в обратном случае.

def is_prime(n):
    sqrt = int(pow(n, 1/2)) + 1
    for i in range(2, sqrt):
        if n % i == 0:
            return False
    return True
    