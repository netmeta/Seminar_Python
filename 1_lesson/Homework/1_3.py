# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

ticket = int(input('Enter ticket number: '))
sum_first = 0
sum_second = 0
while ticket:
    digit = ticket % 10
    if ticket > 999:
        sum_first += digit
    else:
        sum_second += digit
    ticket //= 10
print(f'The ticket is lucky?: {sum_first == sum_second}')

# ----------------------------- 2 solution

ticket_number = input('Enter ticket number: ')
check = ticket_number.isdecimal()

while (ticket_number.__len__() != 6 or check != True):
    print('!! The data is incorrect!')
    ticket_number = input('Enter ticket number: ')
    check = ticket_number.isdecimal()

first_part = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
second_part = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

print(f'The ticket is lucky?: - {first_part == second_part}')
