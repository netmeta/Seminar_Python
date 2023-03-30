# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import choices


num = int(input("Input number of elements in array: "))

list_num = []
for i in range(num):
    list_num.append(int(input(f'Input {i+1} number: ')))

x = int(input('Find number : '))

print('qty', list_num.count(x))

# solution 2

number = int(input("Input number of elements in array: "))
list_nums = choices(range(number*2), k=number)
print(list_nums)
result = list_nums.count(int(input()))
print(result)
