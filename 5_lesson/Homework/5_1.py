# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def pow_num(number, degree):
    if degree == 1:
        return (number)
    if degree != 1:
        return (number * pow_num(number, degree - 1))

print("Result: ", pow_num(number = int(input("Enter number: ")), degree = int(input("Enter its degree: "))))
