# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Enter number: '))
sum_number = 0

while number > 0:
    sum_number += number % 10
    number //= 10

print("Sum of digits :", sum_number)
