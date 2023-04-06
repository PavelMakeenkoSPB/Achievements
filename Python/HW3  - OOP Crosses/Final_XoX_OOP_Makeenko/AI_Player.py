import random
from Base_Player import*

class AI_Player(Base_Player):
        
    def __init__(self, side):
        super().__init__(side)

        
    def AI_Turn(self, field):  # Ход Компьютера

        print('')
        
        if self._side == 2:

            print('Ход Искусcтвенного Разума Обнуляющего! ')

        else:
            print('Ход Искусcтвенного Разума Крестителя! ')
            
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        if self._side == 2:
            print('Я ставлю Нолик в столбец ', x, 'и строку ', y)
            
        else:
            print('Я ставлю Крестик в столбец ', x, 'и строку ', y)

        field[y][x] = self._side

    


