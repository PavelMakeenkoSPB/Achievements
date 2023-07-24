# Чётность всех введённых чисел

n = 10
counter = 0

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        counter += 1

if counter == n:
    print('YES')
else:
    print('NO')



    
    