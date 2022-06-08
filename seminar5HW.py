# № 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
#  записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('33_Polynom.txt', 'w') as data:
    data.write(polynom1)






# № 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
#  чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# with open('ex_35.txt', 'w') as F_N:
#     F_N.write('1 2 3 5 6 7 8 10')
# with open('ex_35.txt') as F_N:
#     my_list = F_N.read() + ' '
#     my_list = list(map(int, my_list.split()))

# def find_number(my_list):
#     result = []
#     for i in range(len(my_list) - 1):
#         if my_list[i+1] - my_list[i] > 1:
#             result.append(my_list[i]+1)
#     return result

# print(find_number(my_list))

# № 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# def unique_elements(list1):
#     return list(filter(lambda x: my_list.count(x) == 1, list1))

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# print(unique_elements(my_list))
