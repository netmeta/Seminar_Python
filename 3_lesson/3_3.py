# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)
list_nums = [0, -1, 5, 2, 3]
print(sum([list_nums[i] > list_nums[i-1] for i in range(0, len(list_nums))]))

m = [0, -1, 5, 2, 3]
count = 0
a = 0
for i in range(0, len(m) - 1, 2):
    if i + 1 > i:
        count += 1
print(count)
