# Дано натуральное число A>1. Определите каким пр счету числом Фибоначчи оно является
# то есть выведите число n, f(n)=A. Если А не фибоначчи выведите -1 ( 5=6)

fib_n = int(input("input fibonacci: "))
count = 2
a = 0
b = 1
while fib_n >= b:
    if fib_n == b:
        print(count)
        break
    a, b = b, a + b
    count += 1
else:
    print(-1)

number = int(input())
result = 1
count = 3
if number == 1:
    print("2b 3")
elif number == 0:
    print("first num")
else:
    while result < number:
        count = + 1
        if result == number:
            break
        result = int(round(1.68*result, 0))
        print(result)
    print("dads", count)
