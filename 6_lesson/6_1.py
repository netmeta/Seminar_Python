# Даны два массива чисел. Требуется вывести те
# элементы первого массива (в том порядке,
# в каком они идут в первом массиве),
# которых нет во втором массиве.
# Пользователь вводит число N - количество
# элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов
# во втором массиве. Затем элементы второго массива
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# [3, 3, 2, 12]
from time import time
from random import choices
start = time()

count1 = int(input('Enter number : '))
list1 = []
for _ in range(count1):
    list1.append(int(input('\telemet massive - ')))
count2 = int(input('Enter number : '))
list2 = []
for _ in range(count2):
    list2.append(int(input('\telemet massive - ')))

print([x for x in list1 if x not in set(list2)])
print(time() - start)
# ------------------------- 2 вариант
_ = input()
n = [int(i) for i in input().split()]

_ = input()
m = [int(j) for j in input().split()]

print(*[i for i in n if i not in m])
print(time() - start)
# ------------------------- 3 вариант

m_dict = {}.fromkeys(m, 1)
print([i for i in n if not m_dict.get(i)])
print(time() - start)