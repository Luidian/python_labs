# Написать функцию, которая принимает 1 аргумент - целое число и возвращает True, если число простое и False в обратном случае.

def isPrime(n):
    # if n == 1
    if n == 2 :
        return True
    if n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i != 0:
            continue
        else:
            return False
    return True


print(isPrime(15))
