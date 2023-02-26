# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 = 2 2
# 5 6 = 2 3

sum_number = int(input("Input first number: "))
product_number = int(input("Input twice number: "))
number_1 = 1

while number_1 < product_number:
    number_2 = sum_number - number_1
    if sum_number == number_1 + number_2 and product_number == number_1 * number_2:
        print(number_1, number_2)
        break
    number_1 += 1
