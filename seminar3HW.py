# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# spisok = [2, 3, 5, 9, 3]
# spisok_b = [v for k,v in enumerate(spisok) if k%2]

# print(sum(spisok_b))

# 2) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Если остается 1 элемент без пары - умножаем его самого на себя.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
# import math
# spisok = [2, 3, 4, 5, 6]
# sum_spisok = []
# a = math.ceil(len(spisok)/2)
# for i in range(a):
#     sum = spisok[i] * spisok[len(spisok)-1-i]
#     sum_spisok.append(sum)
# print(sum_spisok)


# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# a = [1.1, 1.2, 3.1, 5, 10.01]
# float_list = []
# a2 = list(filter(lambda e:isinstance(e, float), a))
# for i in range(len(a2)):
#     float_list.append(round((a2[i] - int(a2[i])),2))
# print(float_list)
# max = max(float_list)
# min = min (float_list)
# result = max - min
# print(result)

