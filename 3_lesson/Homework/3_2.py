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

# solution seminar

list_nums = [randint(1, 50) for _ in range(int(input()))]

print(list_nums)

num = int(input())
right_num = list_nums[0]

for i in list_nums:
    if abs(num - i) < abs(num-right_num):
        right_num = i

print(right_num)

