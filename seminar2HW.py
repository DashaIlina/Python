# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр(отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11
# Не смогла понять как в первом решении b отобразить с тем количеством символом который был задан.
# from math import trunc

# num = float(input("Введите число: ")) 
# a = abs(trunc(num))
# b = round(abs(num) - a)
# print(f"a = {a}")
# print(f"b = {b}")
# mult = 0
# while (a !=0):
#     mult += (a % 10)
#     a = a // 10
# while (b !=0):
#     mult += int(b * 10)
#     b = b * 10 - int(b * 10)
# print(f"Сумма цифр числа {num} = {mult}")

num = str(input("Введите число: "))
sum = 0
for i in num:
    if i != "-" and i != "." and i != ",":
        sum += int(i)
print(f"Сумма цифр числа {num} = {sum}")


# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)
# n = int(input("Введите число: "))
# fact = 1
# list = [1]
# for i in range(2, n+1):
#     fact *= i
#     list.append(fact)
# print(*list)

# 3)Реализуйте случайное перемешивания списка.
# *Пример:*
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True '] Результат -> [250, 3.14, 'True ', 'Веселый пианист']
# import random
# text = ['Веселый пианист', 250, 3.14, 'True ']
# print(text)
# random.shuffle(text)
# print(text)