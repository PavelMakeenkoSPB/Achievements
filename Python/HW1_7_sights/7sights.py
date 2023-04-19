# ============================ Комментарии к комментариям ============================#
# НК - Не Круглое (почти не присутствуюет, поскольку очень частое. Но подразумевается)#
# T11 - Разряд тысяч принимает значения от 11 до 19 включительно или нет (NOT T11)    #
# K11 - разряд десятков принимает значения от 11 до 19 включительно или нет (NOT K11) #
# S7 - седьмой знак, разряд единиц, последний разряд (либо S7 = 0, либо S7 NOT 0)     #
# ====================================================================================#

a = int(input())
st = str(a)  # преобразуем число в строку
char = int(len(list(st)))  # получаем целое количество цифр из длинны массива, составленного из символов введённого числа

if char > 7 or a < 0:  # проверка количества символов более 7 или значения а менее 0
       import sys
       print('Введённое число за гранью наших возможностей')
       sys.exit()  # завершение работы программы при соблюдении условия
       
# ========== Создание списков ==========
fem_units = ['', 'одна', 'две']  # "женские" окончания тысяч
units = ['ноль', 'один', 'два', 'три', 'четыре',
         'пять', 'шесть', 'семь', 'восемь', 'девять']  # разряд единиц
dec = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
       'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']  # разряд десятков
from_11 = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
           'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']  # числа от 11 до 19
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста',
            'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']  # разряд сотен
thousands = ['', 'тысяча', 'тысячи',
             'тысячи', 'тысячи', 'тысяч', 'тысяч', 'тысяч', 'тысяч', 'тысяч']  # разряд тысяч
millions = ['', 'миллион', 'миллиона', 'миллиона', 'миллиона',
            'миллионов', 'миллионов', 'миллионов', 'миллионов', 'миллионов']  # разряд миллионов
# ========== ========= ========== ==========

# Определение каждого символа введённого числа sim7 - единицы, sim1 - миллионы и тп.
sim7 = a % 10
sim6 = (a % 10 ** 2) // 10
sim5 = (a % 10 ** 3) // 10 ** 2
sim4 = (a % 10 ** 4) // 10 ** 3
sim3 = (a % 10 ** 5) // 10 ** 4
sim2 = (a % 10 ** 6) // 10 ** 5
sim1 = (a % 10 ** 7) // 10 ** 6
# Переменные, которые будут иметь значения, если десятки или тысячи будут оканчиваться на 11-19
up11 = 0
up11th = 0

# Проверка на 11-19 в разрядах тысяч и десятков
if sim6 == 1 and 1 <= sim7 <= 9:
       up11 = 10 + sim7  # Определение числа от 11 до 19 в разряде десятков
if sim3 == 1 and 1 <= sim4 <= 9:
       up11th = 10 + sim4  # Определение числа от 11 до 19 в разряде тысяч
    
# =========== Условия при количестве символов 1 ===========
if char == 1:
       if 0 <= a < 10:
              print(units[sim7])

# =========== Условия при количестве символов 2 ===========
if char == 2:
       if a % 10 == 0:  # круглое число
              print(dec[sim6])
       elif a % 10 != 0 and (up11 < 10 or up11 > 19):  # Не круглое(НК), НЕ на 11-19(NOT K11)
              print(dec[sim6], units[sim7])
       elif a % 10 != 0 and 10 < up11 < 20:  # НК, K11
              print(from_11[sim7])

# =========== Условия при количестве символов 3  ===========
if char == 3:
       if a % 100 == 0:  # круглое число
              print(hundreds[sim5])
       elif a % 100 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11 и в конце Не 0(S7 NOT 0)
              print(hundreds[sim5], dec[sim6], units[sim7])
       elif a % 100 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11 и в конце 0(S7 = 0)
              print(hundreds[sim5], dec[sim6])
       elif a % 100 != 0 and 10 < up11 < 20:  # K11
              print(hundreds[sim5], from_11[sim7])

# =========== Условия при количестве символов 4 ===========
if char == 4 and sim4 > 2:  # sim4 символ больше 2, значит не женского рода и не круглое число
       if a % 1000 == 0:  # круглое число
              print(units[sim4], thousands[sim4])
       elif a % 1000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT К11, S7 NOT 0
              print(units[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 1000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT К11, S7 = 0
              print(units[sim4], thousands[sim4], hundreds[sim5], dec[sim6])
       elif a % 1000 != 0 and 10 < up11 < 20:  # К11
              print(units[sim4], thousands[sim4], hundreds[sim5], from_11[sim7])
        
if char == 4 and 0 < sim4 <= 2:  # sim4 в женском роде (одна, две)
       if a % 1000 == 0:  # круглое число
              print(fem_units[sim4], thousands[sim4])
       elif a % 1000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT К11, S7 NOT 0
              print(fem_units[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 1000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT К11, S7 = 0
              print(fem_units[sim4], thousands[sim4], hundreds[sim5], dec[sim6])
       elif a % 1000 != 0 and 10 < up11 < 20:  # К11
              print(fem_units[sim4], thousands[sim4], hundreds[sim5], from_11[sim7])
       elif a % 1000 != 0 and sim6 == 0 and sim7 == 0:  # кгруглые Сотни
              print(fem_units[sim4], thousands[sim4], hundreds[sim5])

# =========== Условия при количестве символов 5 ===========
if char == 5 and sim4 > 2:  # sim4 символ больше 2, значит не женского рода и не круглое число
       if a % 10000 == 0:  # круглое число
              print(dec[sim3], thousands[6])
       elif a % 10000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 != 0:  # Тысячи оканч. на 11-19 (T11), NOT K11, S7 NOT 0
              print(from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 10000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 == 0:  # T11, NOT K11, s7 = 0
              print(from_11[sim4], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 10000 != 0 and 10 < up11th < 20 and 10 < up11 < 20:  # T11, K11
              print(from_11[sim4], thousands[6], hundreds[sim5], from_11[sim7])
       elif a % 10000 != 0 and 10 < up11th < 20:  # T11
              print(from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 10000 != 0 and 10 < up11 < 20:  # K11
              print(dec[sim3], units[sim4], thousands[sim4], hundreds[sim5], from_11[sim7])
       elif a % 10000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(dec[sim3], units[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 10000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(dec[sim3], units[sim4], thousands[sim4], hundreds[sim5], dec[sim6])
        
if char == 5 and 0 < sim4 <= 2:  # "женские" тысячи
       if a % 10000 == 0:  # круглое число
              print(dec[sim3], thousands[6])
       elif a % 10000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 != 0:  # T11, NOT K11, S7 NOT 0
              print(from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 10000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 == 0:  # T11, NOT K11, S7 = 0
              print(from_11[sim4], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 10000 != 0 and 10 < up11th < 20 and 10 < up11 < 20:  # T11, K11
              print(from_11[sim4], thousands[6], hundreds[sim5], from_11[sim7])
       elif a % 10000 != 0 and 10 < up11th < 20:  # T11
              print(from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 10000 != 0 and 10 < up11 < 20:  # K11
              print(dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5], from_11[sim7])
       elif a % 10000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 10000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5], dec[sim6])
        
if char == 5 and sim4 == 0:  # круглые десятки тысяч
       if a % 10000 == 0: # круглое число
              print(dec[sim3], thousands[6])
       elif a % 10000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(dec[sim3], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 10000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(dec[sim3], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 10000 != 0 and 10 < up11 < 20:  # K11
              print(dec[sim3], thousands[6], hundreds[sim5], from_11[sim7])
       elif a % 10000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(dec[sim3], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 10000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(dec[sim3], thousands[6], hundreds[sim5], dec[sim6])

# =========== Условия при количестве символов 6 ===========
if char == 6 and sim4 > 2:
       if a % 100000 == 0:  # круглое число
              print(hundreds[sim2], thousands[6])
       elif a % 100000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 != 0:  # T11, NOT K11, S7 NOT 0
              print(hundreds[sim2], from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 100000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 == 0:  # T11, NOT K11, S7 = 0
              print(hundreds[sim2], from_11[sim4], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 100000 != 0 and 10 < up11th < 20 and 10 < up11 < 20:  # T11, K11
              print(hundreds[sim2], from_11[sim4], thousands[6], hundreds[sim5], from_11[sim7])
       elif a % 100000 != 0 and 10 < up11th < 20:  # T11
              print(hundreds[sim2], from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 100000 != 0 and 10 < up11 < 20:  # K11
              print(hundreds[sim2], dec[sim3], units[sim4], thousands[sim4], hundreds[sim5], from_11[sim7])
       elif a % 100000 != 0 and (up11th < 10 or up11th > 19) and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT T11, NOT K11, S7 NOT 0
              print(hundreds[sim2], dec[sim3], units[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 100000 != 0 and (up11th < 10 or up11th > 19) and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT T11, NOT K11, S7 = 0
              print(hundreds[sim2], dec[sim3], units[sim4], thousands[sim4], hundreds[sim5], dec[sim6])
        
if char == 6 and 0 < sim4 <= 2:  # "женские тысячи"
       if a % 100000 == 0:  # круглое число
              print(hundreds[sim2], thousands[6])
       elif a % 100000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 != 0:  # T11, NOT K11, S7 NOT 0
              print(hundreds[sim2], from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 100000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 == 0:  # T11, NOT K11, S7 = 0
              print(hundreds[sim2], from_11[sim4], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 100000 != 0 and a % 10000 != 0 and 10 < up11th < 20 and 10 < up11 < 20:  # T11, K11
              print(hundreds[sim2], from_11[sim4], thousands[6], hundreds[sim5], from_11[sim7])
       elif a % 100000 != 0 and 10 < up11th < 20:  # T11
              print(hundreds[sim2], from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 100000 != 0 and 10 < up11 < 20:  # K11
              print(hundreds[sim2], dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5], from_11[sim7])
       elif a % 100000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(hundreds[sim2], dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5], dec[sim6])
       elif a % 100000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(hundreds[sim2], dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
        
if char == 6 and sim4 == 0:  # Круглые сотни тысяч
       if a % 100000 == 0:  # круглое число
              print(hundreds[sim2], thousands[6])
       elif a % 100000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(hundreds[sim2], dec[sim3], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 100000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(hundreds[sim2], dec[sim3], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 100000 != 0 and 10 < up11 < 20:  # K11
              print(hundreds[sim2], dec[sim3], thousands[6], hundreds[sim5], from_11[sim7])

# =========== Условия при количестве символов 7 ===========
if char == 7 and sim4 > 2:
       if a % 1000000 == 0:  # круглое число
              print(units[sim1], millions[sim1])
       elif a % 1000000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 != 0:  # T11, NOT K11, S7 NOT 0
              print(units[sim1], millions[sim1], hundreds[sim2],
              from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 1000000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 == 0:  # T11, NOT K11, S7 = 0
              print(units[sim1], millions[sim1], hundreds[sim2],
              from_11[sim4], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 1000000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(units[sim1], millions[sim1], hundreds[sim2],
              dec[sim3], units[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 1000000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(units[sim1], millions[sim1], hundreds[sim2],
              dec[sim3], units[sim4], thousands[sim4], hundreds[sim5], dec[sim6])
       elif a % 1000000 != 0 and 10 < up11th < 20 and 10 < up11 < 20:  # T11, K11
              print(units[sim1], millions[sim1], hundreds[sim2],
              from_11[sim4], thousands[sim4], hundreds[sim5], from_11[sim7])
       elif a % 1000000 != 0 and 10 < up11th < 20:  # T11
              print(units[sim1], millions[sim1], hundreds[sim2],
              from_11[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 1000000 != 0 and 10 < up11 < 20:  # K11
              print(units[sim1], millions[sim1], hundreds[sim2], dec[sim3], units[sim4], thousands[sim4], hundreds[sim5],
              from_11[sim7])
        
if char == 7 and 0 < sim4 <= 2:  # "женские" тысячи
       if a % 1000000 == 0:  # круглое число
              print(units[sim1], millions[sim1])
       elif a % 1000000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 != 0:  # T11, NOT K11, S7 NOT 0
              print(units[sim1], millions[sim1], hundreds[sim2],
              from_11[sim4], thousands[6], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 1000000 != 0 and (10 < up11th < 20) and (up11 < 10 or up11 > 19) and sim7 == 0:  # T11, NOT K11, S7 = 0
              print(units[sim1], millions[sim1], hundreds[sim2],
              from_11[sim4], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 1000000 != 0 and 10 < up11th < 20 and 10 < up11 < 20:  # T11, K11
              print(units[sim1], millions[sim1], hundreds[sim2],
              from_11[sim4], thousands[6], hundreds[sim5], from_11[sim7])
       elif a % 1000000 != 0 and 10 < up11th < 20:  # T11
              print(units[sim1], millions[sim1], hundreds[sim2],
              from_11[sim4], thousands[sim4], hundreds[sim5], dec[sim6], units[sim7])
       elif a % 1000000 != 0 and 10 < up11 < 20:  # K11
              print(units[sim1], millions[sim1], hundreds[sim2], dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5],
              from_11[sim7])
       elif a % 1000000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(units[sim1], millions[sim1], hundreds[sim2], dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5],
              dec[sim6])
       elif a % 1000000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(units[sim1], millions[sim1], hundreds[sim2], dec[sim3], fem_units[sim4], thousands[sim4], hundreds[sim5],
              dec[sim6], units[sim7])

if char == 7 and sim4 == 0:  # Круглые сотни тысяч
       if a % 1000000 == 0:  # круглое число
              print(units[sim1], millions[sim1])
       elif a % 1000000 != 0 and (up11 < 10 or up11 > 19) and sim7 != 0:  # NOT K11, S7 NOT 0
              print(units[sim1], millions[sim1], hundreds[sim2], dec[sim3], thousands[6], hundreds[sim5], dec[sim6],
              units[sim7])
       elif a % 1000000 != 0 and (up11 < 10 or up11 > 19) and sim7 == 0:  # NOT K11, S7 = 0
              print(units[sim1], millions[sim1], hundreds[sim2], dec[sim3], thousands[6], hundreds[sim5], dec[sim6])
       elif a % 1000000 != 0 and 10 < up11 < 20:  # K11
              print(units[sim1], millions[sim1], hundreds[sim2], dec[sim3], thousands[6], hundreds[sim5], from_11[sim7])

