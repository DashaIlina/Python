# № 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
#  записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# def get_polynom(degree):
#     polynom_str = ''
#     for n in range(degree, 0, -1):
#         a = random.randint(0, 100)
#         if a != 0:
#             if n == degree and n != 1:
#                 polynom_str += str(a) + 'x^' + str(n)
#             elif n == degree and n == 1:
#                 polynom_str += str(a) + 'x'
#             elif n == 1:
#                 polynom_str += '+' + str(a) + 'x^'
#             else:






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
