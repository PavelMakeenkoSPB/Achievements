# Максимальные числа

n = int(input('input amount '))
bigger = 0
maximal = 0

for z in range(n):

    number = int(input())
    if number > maximal:

        bigger = maximal
        maximal = number


    elif number > bigger:

        bigger = number


print(maximal)
print(bigger)


    