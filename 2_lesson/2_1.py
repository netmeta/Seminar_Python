# По данному целому неотрицательному n вычислите знаяение n!.N!=1*2*3*...*N
# использовать while 5!=120
# factorial

n = int(input())
count = 1
result = 1
while n >= count:
    result *= count
    count += 1

print(result)

n = int(input())
fact_n = 1
n += 1
while n > 1:
    fact_n *= n-1
    n -= 1
print(fact_n)
