# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# функция  .split()

text_list = input().split()
my_dict = {}

for i in text_list:
    if i in my_dict:
        print(f'{i}_{my_dict[i]}', end=' ')
    else:
        print(i, end=' ')
    my_dict[i] = my_dict.get(i, 0) + 1

# solution 2

chars = input().split()
dict_chars = {}.fromkeys(chars, 0)
print(dict_chars)

for i in chars:
    print(f'{i}_{dict_chars[i]}' if dict_chars[i] else i, end=' ')
    dict_chars[i] += 1
