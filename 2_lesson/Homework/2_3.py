# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N. 10 = 1 2 4 8

number = int(input())
degree = 1

while degree <= number:
    print(degree, end=" ")
    degree *= 2
