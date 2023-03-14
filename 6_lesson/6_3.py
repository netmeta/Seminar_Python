# Дан список чисел. Посчитайте,
# сколько в нем пар элементов,
# равных друг другу.
# Считается, что любые два элемента,
# равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел.
# Все числа списка находятся на разных строках.

from time import time
from random import choices
# import random as rd

# list_1 = [i for i in range(2, 10)]

# rd.shuffle(list_1)

# for num in list_1:
#     print(num, end=' ')
list_1 = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3]
print(list_1)
list_2 = list(set(list_1))
print(f'list2', list_2)
count = 0
for i in range(len(list_2)):
    count += list_1.count(list_2[i]//2)
print(count)
list_1 = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3]
dict_list = {}.fromkeys(list_1, 0)
print(dict_list)
for i in list_1:
    dict_list[i] += 1
print(sum([i//2 for i in dict_list.values() if not i % 2]))

# solution 2
li = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3, 3, 3,6]
sum = 0
for i in li:
    a=li.count(i)
    if a > 1:
        if a % 2 != 0:
            sum += (a - 1) / 2
            li.pop(i)
        else:
            sum += a / 2
        print(f'i = {a / 2}, sum = {sum/4}')



nums = [int(i) for i in input().split()]
# nums = choices(range(3000), k=2000)

# start = time()
m_dict = {}.fromkeys(nums, 0)

for j in nums:
    m_dict[j] += 1

num_count = [i // 2 for i in m_dict.values() if not i % 2]
print(sum(num_count))


# print(time() - start)