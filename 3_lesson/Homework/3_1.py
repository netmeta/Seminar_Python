# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1



number = int(input("Input number of elements in array: "))
list_1 = []

for i in range(1, number+1):
    list_1.append(i)

print(list_1)
print(list_1.count(int(input())))


# solution seminar

from random import choices

number = int(input("Input number of elements in array: "))
list_nums = choices(range(number*2), k=number)
print(list_nums)
result = list_nums.count(int(input()))
print(result)
