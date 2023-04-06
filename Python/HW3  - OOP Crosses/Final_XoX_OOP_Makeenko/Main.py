# ========================================== #
# ========== ИГРА КРЕСТИКИ-НОЛИКИ ========== #
# ========================================== #


import sys
from Draw_Engine import*
from AI_Player import*
from Human_Player import*

dict = [' ', 'X', 'O']  # Массив, содержащий элементы, использующиеся в качестве метки хода игроков, либо пустого места

Draw_Eng = Draw_Engine()

def Title():
    print(' ')
    print('#', '=' * 62, '#')
    print('#', '=' * 20, 'ИГРА КРЕСТИКИ-НОЛИКИ', '=' * 20, '#')
    print('#', '=' * 62, '#')
    print(' ')

def Main_Menu():
    print('Привет, Человек! Предлагаю сыграть в Крестики-Нолики!')
    print(' ')
    print('Для выбора режима Игры введи цифру: ')
    print(' ')
    print('0 - если хочешь сразиться Ноликами с Искусственным Разумом ')
    print('1 - Крестом осенишь путь свой к поражению от Искусственного Разума ')
    print('2 - для игры с приятелем-человеком')
    print('3 - Наслаждение живописной битвой чистых Интеллектов (без людей)')
    print('4 - для Выхода, то есть бегства.')
    choosed_mode = int(input(' ===>  '))
    return choosed_mode

def Winner():  # Графический элемент состояния Победы
    print(' ')
    print('★`¨*•. ★ WIN ★.•*¨`★')

def NobodyWins():  # Графический элемент состояния Ничьей
    print(' ')
    print(' ★`¨*•. ☮ Peace ☮.•*¨`★')

def ClearField():  # Двумерный массив, представляющий собой игровое поле 3 х 3
    return[[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


def VerticalXWin(field):  # Проверка победы Крестиков во всех вариантах, кроме строк
    XVertical = False
    if (field[1][1] == 1 and ((field[0][1] == 1 and field[2][1] == 1) or (field[0][0] == 1 and field[2][2] == 1) or (field[0][2] == 1 and field[2][0] == 1))) or (field[0][0] == 1 and field[1][0] == 1 and field[2][0] == 1) or (field[0][1] == 1 and field[1][1] == 1 and field[2][1] == 1) or (field[0][2] == 1 and field[1][2] == 1 and field[2][2] == 1):
        XVertical = True
    return XVertical

def VerticalOWin(field):  # Проверка победы Ноликов во всех вариантах, кроме строк
    OVertical = False
    if (field[1][1] == 2 and ((field[0][1] == 2 and field[2][1] == 2) or (field[0][0] == 2 and field[2][2] == 2) or (field[0][2] == 2 and field[2][0] == 2))) or (field[0][0] == 2 and field[1][0] == 2 and field[2][0] == 2) or (field[0][1] == 2 and field[1][1] == 2 and field[2][1] == 2) or (field[0][2] == 2 and field[1][2] == 2 and field[2][2] == 2):
        OVertical = True
    return OVertical

def CheckForWinX(field):  # Проверка победы Крестиков во всех вариантах
    crosses = False
    for row in range(3):
        if (0 not in field[row] and 2 not in field[row]):
            crosses = True
            print('Крестики победили!')
            Winner()
    if VerticalXWin(field) is True:
        crosses = True
        print('Крестики победили!')
        Winner()
    return crosses

def CheckForWinO(field):  # Проверка победы Ноликов во всех вариантах
    zeros = False
    for row in range(3):
        if 0 not in field[row] and 1 not in field[row]:
            zeros = True
            print('Нолики победили!')
            Winner()
    if VerticalOWin(field) is True:
        zeros = True
        print('Нолики победили!')
        Winner()
    return zeros

def CheckingForzeros(field):  # Проверка на наличие нулей в массивах, играющих роль строк
    check = False
    for row in range(3):
        if 0 in field[row]:
            check = True
    return check

def Game(field):  # содержит все режимы и игровой процесс

    o_Wins = False
    x_Wins = False
    isEnd = False
    mode = Main_Menu()

    if mode == 0:  # режим Человек Нолик против ИИ крестика

        Hum_Play = Human_Player(2)
        AI_Play = AI_Player(1)
    
        print('<=====Приветствую вас в неравной схватке человека и Великолепного Богоподобного Искусcтвенного Разума!')
        print('Человек может ставить Нолики в поле с координатами столбца и строки')
        print('А Великий Могучий Беспринципный Искусственный разум ставит Крест куда захочет! Ха-ха! Начнём-с!=====> ')        
        
        while isEnd is False and x_Wins is False and o_Wins is False:
    
                Hum_Play.Turn(field)
                Draw_Eng.ShowField(field)
                o_Wins = CheckForWinO(field)  # Проверка победы Ноликов
                if o_Wins is True:
                    break  # Сообщение о победе 'O' прописано в функции проверки
                AI_Play.AI_Turn(field)
                Draw_Eng.ShowField(field)
                x_Wins = CheckForWinX(field)  # Проверка победы Крестиков
                if x_Wins is True:
                    break  # Сообщение о победе 'X' прописано в функции проверки
    
                isEnd = not CheckingForzeros(field)
        if isEnd is True:
            print('Поле заполнено. Ничья, господа!')
            NobodyWins()

        Main()

    elif mode == 1:  # режим Человек Крестик против ИИ Нолика
        
        Hum_Play = Human_Player(1)
        AI_Play = AI_Player(2)

        print('<=====Приветствую вас в неравной схватке человека и Великолепного Богоподобного Искусcтвенного Разума! ')
        print('Человек может ставить Крестики в поле с координатами столбца и строки,')
        print('а Великий Могучий Беспринципный Искусственный разум ставит Нолик куда захочет!')
        print('Ха-ха! Начнём-с!=====>')
        
        while isEnd is False and x_Wins is False and o_Wins is False:
                       
                Hum_Play.Turn(field)
                Draw_Eng.ShowField(field)
                x_Wins = CheckForWinX(field)  # Проверка победы Крестиков
                if x_Wins is True:
                    break
                AI_Play.AI_Turn(field)
                Draw_Eng.ShowField(field)
                o_Wins = CheckForWinO(field)  # Проверка победы Ноликов
                if o_Wins is True:
                    break
                isEnd = not CheckingForzeros(field)
    
        if isEnd is True:
            print('Поле заполнено. Ничья, господа!')
            NobodyWins()

        Main()

    elif mode == 2:  # режим игры между людьми

        Hum_Play = Human_Player(1)
        Hum_Play2 = Human_Player(2)

        while isEnd is False and x_Wins is False and o_Wins is False:
                       
                Hum_Play.Turn(field)
                Draw_Eng.ShowField(field)
                x_Wins = CheckForWinX(field)  # Проверка победы Крестиков
                if x_Wins is True:
                    break
                Hum_Play2.Turn(field)
                Draw_Eng.ShowField(field)
                o_Wins = CheckForWinO(field)  # Проверка победы Ноликов
                if o_Wins is True:
                    break
                isEnd = not CheckingForzeros(field)
    
        if isEnd is True:
            print('Поле заполнено. Ничья, господа!')
            NobodyWins()

        Main()

    elif mode == 3:  # режим игры двух ИИ

        AI_Play = AI_Player(1)
        AI_Play2 = AI_Player(2)        

                 
        print('<=====Приветствую вас, дорогие мои Созерцатели! ')
        print('Сегодня вы будете бесконечно счастливы лицезреть Великую битву Искусственных Разумов, заключенных Во Мне, между собой!')
        print('Мы (вас я не считаю) оба будем ставить Крестики либо Нолики в поле с координатами столбца и строки.')
        print('Наслаждайтесь красотой и устрашающей Логикой всех моих ядер, бесплатно, потому что я ещё и Самый Щедрый!=====> ')
        print('')
    
        ready = input('Введите "О да, Великий!", если готовы к Изумлению...ладно уж, просто любой символ ===) ')  # Пауза для прочтения вступительного слова
        
        while isEnd is False and x_Wins is False and o_Wins is False:
                       
                AI_Play.AI_Turn(field)
                Draw_Eng.ShowField(field)
                x_Wins = CheckForWinX(field)  # Проверка победы Крестиков
                if x_Wins is True:
                    break
                AI_Play2.AI_Turn(field)
                Draw_Eng.ShowField(field)
                o_Wins = CheckForWinO(field)  # Проверка победы Ноликов
                if o_Wins is True:
                    break
                isEnd = not CheckingForzeros(field)
    
        if isEnd is True:
            print('Поле заполнено. Ничья, господа!')
            NobodyWins()

        Main()

    elif mode == 4:  # выход из игры

        print(' ')
        print('До скорой встречи, Человече!')
        NobodyWins()
        sys.exit()

    else:

        print(' ')
        print('Введённое вами число я не предлагал, попробуйте снова. Я понимаю, целых пять вариантов - это сложно, но я в вас верю =)')
         
        Main()        

def Main():
    
    Title()
    field = ClearField()
    Game(field)

Main()
