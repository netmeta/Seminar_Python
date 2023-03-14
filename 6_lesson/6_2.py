# Напишите программу, которая в данном
# массиве определит количество элементов,
# у которых два соседних и, при этом,
# оба соседних элемента меньше данного.

# Сначала вводится число N — количество
# элементов в массиве. Далее записаны N
# чисел — элементы массива.
# Массив состоит из целых чисел.

list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 5, 1, 5, 1]
list_3 = []
count_1 = 0
n = int(input('Введите количество элементов первого массива: '))
for i in range(n):
    list_1.append(int(input('Введите элемент 1-ого массива: ')))
for i in range(1, len(list_1)-1):
    if (list_1[i] > list_1[i+1]) & (list_1[i] > list_1[i-1]):
        count_1 += 1
print(count_1)

# solution 2

list_1 = [1, 5, 1, 5, 1]
count_1 = 0
for i in range(1, len(list_1)-1):
    if list_1[i] == max(list_1[i-1:i+2]):
        count_1 += 1
print(count_1)

print(len([i for i in range(1, len(list_1)-1) if list_1[i] == max(list_1[i-1:i+2])]))

print(len([i for i in range(1, len(list_1)-1) if list_1[i-1] < list_1[i] > list_1[i+1]]))

# ------------------------- 4 вариант
_ = input()
nums = [int(i) for i in input().split()]

count = 0
for i in range(1, len(nums) - 1):
    if nums[i] == max(nums[i - 1: i + 2]):
        count += 1

print(count)

# ------------------------- 4 вариант

print(len([i for i in range(1, len(nums) - 1) if nums[i - 1] < nums[i] > nums[i + 1]]))