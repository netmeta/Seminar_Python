# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input())
num_sum = 0

while num:
    num_sum += num % 10
    num //= 10

print(num_sum)
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
count = int(input())

if count % 6:
    print("The data is incorrect!")
else:
    k = 2 * count // 3
    p = s = count // 6
    print(p, k, s)
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

ticket_number = int(input())

sum_first = 0
sum_last = 0

while ticket_number:
    digit = ticket_number % 10
    if ticket_number > 999:
        sum_first += digit
    else:
        sum_last += digit
    ticket_number //= 10
print(f"The ticket is lucky: {sum_first==sum_last}")

# -----------------solution 2
ticket_number = input()
sum_first = int(ticket_number[0] + ticket_number[1] + ticket_number[2])
sum_last = int(ticket_number[3] + ticket_number[4] + ticket_number[5])
print(f"The ticket is lucky: {sum_first==sum_last}")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

