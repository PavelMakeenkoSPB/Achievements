from Base_Player import *


class Human_Player(Base_Player):
   

    def __init__(self, side):
            super().__init__(side)
           
    def Turn(self, field):  # Ход Игрока
       
        print('')
       
        if self._side == 1:
            print('Ваш ход, Игрок за Крестики! ')

        else:

            print('Ваш ход, Игрок за Нолики! ')

        x = int(input('Введите номер колонки: 0, 1 или 2 ==> '))
        y = int(input('Введите номер строки: 0, 1 или 2 ==> '))

        if self._side == 1:
            print('Игрок за Крестики, Вы походили Крестиком на столбец: ', x, 'и строку', y)
            
        else:
            print('Игрок за Нолики, Вы походили Ноликом на столбец: ', x, 'и строку', y)

        field[y][x] = self._side
