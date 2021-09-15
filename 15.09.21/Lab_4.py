import ast
v_2 = []
v_1 = []
print("Введите вектор 1")
for i in range(3):
    v_1.append(ast.literal_eval(input()))
print("Введите вектор 2")
for i in range(3):
    v_2.append(ast.literal_eval(input()))

v_3 = []
for i, j in zip(v_1, v_2):
    v_3.append(i+j)

print(v_3)

# 3 5 1
# 7 5 9
# 10 10 10

