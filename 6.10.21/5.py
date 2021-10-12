# Написать функцию, которая вычисляет среднее арифмитическое чисел в последовательности. 
# Последовательность чисел передаётся через аргумент.

def arithmetic_mean(s):
    temp = 0
    for i in s:
        temp +=i
    return temp/len(s)


s = [1, 2, 3, 4] # 2.5
print(arithmetic_mean(s))