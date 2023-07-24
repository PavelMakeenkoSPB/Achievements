# Нахождение суммы всех множителей целого числа

n = int(input())
counter = 0

for i in range(1, n + 1):
    if n % i == 0:
        counter += i

print(counter)
    
    