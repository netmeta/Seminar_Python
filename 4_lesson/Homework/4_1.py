# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint

n1, m1 = input().split()
first = [int(i) for i in input().split()]
second = [int(j) for j in input().split()]

print(*sorted(set(first).intersection(second)))

# solution 2

n = int(input('Введите число N: '))
m = int(input('введите число M: '))

list_1 = [randint(0,50) for i in range(n)]
list_2 = [randint(0,50) for i in range(m)]

result = set(list_1 + list_2)
print(sorted(result))