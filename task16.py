# Требуется вычислить, сколько раз встречается некоторое число X в массиве 
# из случайных чисел. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input())
sequence = list(map(int, input().split()))
print(sequence)
x = int(input())
count = 0
i = 0
for i in sequence:
    if i == x:
        count += 1
print(count)
