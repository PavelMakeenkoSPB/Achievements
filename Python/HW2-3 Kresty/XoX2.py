# ========================================== #
# ========== ИГРА КРЕСТИКИ-НОЛИКИ ========== #
# ========================================== #

import random
import sys

dict = [' ', 'X', 'O']  # Массив, содержащий элементы, использующиеся в качестве метки хода игроков, либо пустого места

def Hello():
    print(' ')
    print('#', '=' * 42, '#')
    print('#', '=' * 10, 'ИГРА КРЕСТИКИ-НОЛИКИ', '=' * 10, '#')
    print('#', '=' * 42, '#')
    print(' ')

def Question():  # Выбор режима игры
    FirtQuestion = int(input('Привет, Человек! Предлагаю сыграть в Крестики-Нолики. Если хочешь сразиться с Искусственным Разумом Ноликами - набери "0", если Крестиками - набери "1". Для игры с другим Человеком - набери "2", а если тебе лень думать, и ты хочешь увидеть битву настоящих Интеллектов - набери "3" и будет игра между Искусcтвенными Разумами. Для выхода, введи "4", что в азиатской культуре означает смерть. Ваш выбор ===>  '))
    return FirtQuestion

def GetFieldPos(field, row, column):  # Определение координат хода
    fpos = field[row][column]
    return dict[fpos]

def ShowField(field):  # Отрисовка поля и расстановка мест хода игроков
    for row in range(3):
        print('-' * 13)
        for column in range(3):
            print(f'| {GetFieldPos(field, row, column)} ', end='')
        print('|')
    print('-'*13)

def ClearField():  # Двумерный массив, представляющий собое игровое поле 3 х 3
    return[[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

def Krasota():  # Элементы псевдографики для визуального разделения партий
    print(' ')
    print('#', '=X=O' * 11, '=', '#', sep='')
    print(' ')

def Player(field):  # Ход Икгрока за Крестики
    print('Ваш ход, Игрок за Крестики! ')
    x = int(input('Введите номер колонки: 0, 1 или 2 ==> '))
    y = int(input('Введите номер строки: 0, 1 или 2 ==> '))
    print('Игрок за Крестики, Вы походили Крестиком на столбец: ', x, 'и строку', y)
    field[y][x] = 1
    
def PlayerTWO(field):  # Ход Игрока за Нолики
    print('Ваш ход, Игрок за Нолики! ')
    x = int(input('Введите номер колонки: 0, 1 или 2 ==> '))
    y = int(input('Введите номер строки: 0, 1 или 2 ==> '))
    print('Игрок за Нолики, Вы походили Ноликом на столбец: ', x, 'и строку', y)
    field[y][x] = 2

def AITurn(field):  # Ход Первого Компьютера, Нолика
    print('Ход Искуственного Разума Обнуляющего! ')
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    field[y][x] = 2
    print('Я ставлю Нолик в столбец ', x, 'и строку ', y)

def AITWOTurn(field):  # Ход Второго Компьютера, Крестика
    print('Ход Искуственного Разума Крестителя! ')
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    field[y][x] = 1
    print('Я ставлю Крестик в столбец ', x, 'и строку ', y)

def VerticalXXXWin(field):  # Проверка победы Крестиков во всех вариантах, кроме строк
    XVertical = False
    if (field[1][1] == 1 and ((field[0][1] == 1 and field[2][1] == 1) or (field[0][0] == 1 and field[2][2] == 1) or (field[0][2] == 1 and field[2][0] == 1))) or (field[0][0] == 1 and field[1][0] == 1 and field[2][0] == 1) or (field[0][1] == 1 and field[1][1] == 1 and field[2][1] == 1) or (field[0][2] == 1 and field[1][2] == 1 and field[2][2] == 1):
        XVertical = True
    return XVertical

def VerticalOOOWin(field):  # Проверка победы Ноликов во всех вариантах, кроме строк
    OVertical = False
    if (field[1][1] == 2 and ((field[0][1] == 2 and field[2][1] == 2) or (field[0][0] == 2 and field[2][2] == 2) or (field[0][2] == 2 and field[2][0] == 2))) or (field[0][0] == 2 and field[1][0] == 2 and field[2][0] == 2) or (field[0][1] == 2 and field[1][1] == 2 and field[2][1] == 2) or (field[0][2] == 2 and field[1][2] == 2 and field[2][2] == 2):
        OVertical = True
    return OVertical

   

def CheckForWinXXX(field):  # Проверка победы Крестиков во всех вариантах
    XXX = False
    for row in range(3):
        if (0 not in field[row] and 2 not in field[row]):
            XXX = True
            print('Крестики победили!')
    if VerticalXXXWin(field) is True:
        XXX = True
        print('Крестики победили!')            
    return XXX

def CheckForWinOOO(field):  # Проверка победы Ноликов во всех вариантах
    OOO = False
    for row in range(3):
        if 0 not in field[row] and 1 not in field[row]:
            OOO = True
            print('Нолики победили!')
    if VerticalOOOWin(field) is True:
        OOO = True
        print('Нолики победили!')
    return OOO

def Game_Player_VS_AI(field):  # Игра Человека против Компьютера
    Krasota()
    print('<=====Приветствую вас в неравной схватке человека и Великолепного Богоподобного Искуственного Разума! Человек может ставить Крестики в поле с координатами столбца и строки, а Великий Могучий Беспринципный Искусственный разум ставит Нолик куда захочет! Ха-ха! Начнём-с!=====> ')
    OOOWins = False
    XXXWins = False
    isEnd = False
    while isEnd is False and XXXWins is False and OOOWins is False:
            Player(field)
            ShowField(field)
            XXXWins = CheckForWinXXX(field)  # Проверка победы Крестиков
            if XXXWins is True:
                break
            AITurn(field)
            ShowField(field)
            OOOWins = CheckForWinOOO(field)  # Проверка победы Ноликов
            if OOOWins is True:
                break
            isEnd = not CheckingForZero(field)
    if isEnd is True:
        print('Поле заполнено. Ничья, господа!')
    Krasota()
    Main()

def Game_AI_VS_Player(field):  # Игра Компьютера за Крестики против Человека за Нолики
    Krasota()
    print('<=====Приветствую вас в неравной схватке человека и Великолепного Богоподобного Искуственного Разума! Человек может ставить Нолики в поле с координатами столбца и строки, а Великий Могучий Беспринцыпный Искусственный разум ставит Крест куда захочет! Ха-ха! Начнём-с!=====> ')
    OOOWins = False
    XXXWins = False
    isEnd = False
    while isEnd is False and XXXWins is False and OOOWins is False:

            AITWOTurn(field)
            ShowField(field)
            XXXWins = CheckForWinXXX(field)  # Проверка победы Крестиков
            if XXXWins is True:
                break
            
            PlayerTWO(field)
            ShowField(field)
            OOOWins = CheckForWinOOO(field)  # Проверка победы Ноликов
            if OOOWins is True:
                break            
            isEnd = not CheckingForZero(field)
    if isEnd is True:
        print('Поле заполнено. Ничья, господа!')
    Krasota()
    Main()

def Game_Player1_VS_Player2(field):  # Игра между Людьми
    Krasota()
    print('<=====Приветсвую вас, дорогие мои человечки! Вы оба можете ставить Крестики либо Нолики в поле с координатами столбца и строки. Играйте, наслаждайтесь, используйте мой Невероятный Разум для примитивной игры, для которой вы ухитрились не найти бумажку и карандаш! К Вашим услугам все мои 8 ядер!=====> ')
    OOOWins = False
    XXXWins = False
    isEnd = False
    while isEnd is False and XXXWins is False and OOOWins is False:
            Player(field)
            ShowField(field)
            XXXWins = CheckForWinXXX(field)  # Проверка победы Крестиков
            if XXXWins is True:
                break
            PlayerTWO(field)
            ShowField(field)
            OOOWins = CheckForWinOOO(field)  # Проверка победы Ноликов
            if OOOWins is True:
                break
            isEnd = not CheckingForZero(field)
    if isEnd is True:
        print('Поле заполнено. Ничья, господа!')
    Krasota()
    Main()    

def Game_AI_VS_AI(field):  # Игра Компьютера с самим собой
    Krasota()
    print('<=====Приветствую вас, дорогие мои Созерцатели! Сегодня вы должны быть бесконечно счастливы лицезреть Великую битву Искусственных Разумов, заключенных Во Мне, между собой! Мы (вас я не считаю) оба будем ставить Крестики либо Нолики в поле с координатами столбца и строки. Наслаждайтесь красотой и устрашающей Логикой всех моих ядер, бесплатно, потому что я ещё и Самый Щедрый!=====> ')

    OOOWins = False
    XXXWins = False
    isEnd = False
    while isEnd is False and XXXWins is False and OOOWins is False:
            
            AITWOTurn(field)
            ShowField(field)
            XXXWins = CheckForWinXXX(field)  # Проверка победы Крестиков
            if XXXWins is True:
                break
            
            AITurn(field)
            ShowField(field)
            OOOWins = CheckForWinOOO(field)  # Проверка победы Ноликов
            if OOOWins is True:
                break            

           
            isEnd = not CheckingForZero(field)
    if isEnd is True:
        print('Поле заполнено. Ничья, господа Компьютеры!')
    Krasota()
    Main()

def CheckingForZero(field):  # Проверка на наличие нулей в массивах, играющих роль строк
    check = False
    for row in range(3):              
        if 0 in field[row]:
            check = True
    return check
            

def Main():
    Hello()
    field = ClearField()
    AnswerOfPlayer = Question()
    if AnswerOfPlayer == 1:
        Game_Player_VS_AI(field)
    elif AnswerOfPlayer == 0:
        Game_AI_VS_Player(field)
    elif AnswerOfPlayer == 2:
        Game_Player1_VS_Player2(field)
    elif AnswerOfPlayer == 3:
        Game_AI_VS_AI(field)
    elif AnswerOfPlayer == 4:
        sys.exit()
    else:
        print('Введённое вами число я не предлагал, попробуйте снова. Я понимаю, целых пять вариантов - это сложно, но я в вас верю =)')
        Krasota()
        Main()

Main()
