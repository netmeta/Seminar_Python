# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X`

from random import randint

element = int(input('Enter the number of elements: '))
find_element = int(input('Enter a number to search: '))
arr = []

for i in range(1, element+1):
    arr.append(i)
    print(i, end=" ")

eps = find_element
result = arr[0]
for i in arr:
    if abs(i - find_element) < eps:
        eps = abs(i - find_element)
        result = i
print()
print(f"Closest element: {result}")
result = min(arr, key=lambda y: abs(find_element - y))
print(f"Closest element option 2: {result}")

# solution 2

num = int(input('Введите кол-во элементов массива: '))
x = int(input('Введите число X: '))

list_nums = [randint(1,50) for i in range(num)]
res_index, diff = 0, abs(list_nums[0] - x)

for i in range(1, num):
    if abs(list_nums[i] - x) < diff:
        diff, res_index = abs(list_nums[i] - x), i
        
print(list_nums)
print('{} - ближайший элемент в массиве к числу {}' .format(list_nums[res_index],x))

