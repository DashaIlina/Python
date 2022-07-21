# 1.Напишите программу, удаляющую из текста все слова, содержащие "абв".
# def del_some_words(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return " ".join(text)
# my_text = 'Напишите программу, удаляющую из текста все слова, содержащие абв'
# print(del_some_words(my_text))

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


# 3.Создайте программу для игры в "Крестики-нолики".


def krestiki():
    pole = [ ['-','-','-'], 
            ['-','-','-'], 
            ['-','-','-'], 
            ]
    count = 0
    
    
    while count < 9:
        if count % 2 == 0: 
            sign = 0
            player = 1
        else: 
            sign = 1
            player = 2
        step_in_row = int(input(f'{player} Игрок введите номер строки '))
        step_in_column = int(input(f'{player} Игрок введите номер столбца '))
                
        count += 1
        if pole[step_in_row-1][step_in_column-1] == '-':
            pole[step_in_row-1][step_in_column-1] = sign
        else: 
            while pole[step_in_row-1][step_in_column-1] != '-':
                print("Введите другие координаты")
                step_in_row = int(input(f'{player} Игрок введите номер строки '))
                step_in_column = int(input(f'{player} Игрок введите номер столбца '))
            pole[step_in_row-1][step_in_column-1] = sign
        for i in pole:print(i) 
        for i in range(3):
            if (pole[0][i]== 1 and pole[1][i]== 1 and pole[2][i] == 1) or ( pole[i][0]== 1 and pole[i][1]== 1 and pole[i][2] == 1) :
                print ("выиграл 2 игрок") 
                return 
            elif (pole[0][i]== 0 and pole[1][i]== 0 and pole[2][i] == 0) or ( pole[i][0]== 0 and pole[i][1]== 0 and pole[i][2] == 0):
                print ("выиграл 1 игрок")
                return
        if (pole[0][0]== 1 and pole[1][1]== 1 and pole[2][2] == 1) or (pole[0][2]== 1 and pole[1][1]== 1 and pole[2][0] == 1):
            print ("выиграл 2 игрок")
            return
        elif (pole[0][0]== 0 and pole[1][1]== 0 and pole[2][2] == 0) or (pole[0][2]== 0 and pole[1][1]== 0 and pole[2][0] == 0):
            print ("выиграл 1 игрок")
            return
        if count == 9:
            print("Победителей нет")
krestiki()



# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.