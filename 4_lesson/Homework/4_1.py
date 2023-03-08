# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()

a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)

b = [int(x) for x in input().split()]
k1 = set(b)

for i in k1:
    set_2.add(i)

lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')


# solution 2
n, m = input().split()
first = [int(i) for i in input().split()]
second = [int(j) for j in input().split()]

print(*sorted(set(first).intersection(second)))
