# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5-> 1 0 1 1 0
# 2шт

number = int(input("Input number of coins:  "))
count_side = 0

for i in range(number):
    side_coins = int(input("Input side: "))
    if side_coins:
        count_side += 1

if count_side > number // 2:
    count_side = number - count_side

print(count_side)
