# Пользователь вводит текст.
# Вывести самое длинное слово и наиболее часто встречаемое слово.

s = input('Введите текст') # т.к. не описано, предпологается, что текст одного регистра и не имеет знаков препинания

words = s.split(' ')

print(sorted(words, key=len)[-1])

often = words[0]
for i in set(words):
    if words.count(i) > words.count(often):
        often = i
print(often)
