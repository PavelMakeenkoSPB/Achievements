# Фибоначчи


numberOfSteps = int(input())

first = 1
second = 1
amountFirstSecond = 0

for _ in range(numberOfSteps):

    first = second
    second = amountFirstSecond
    amountFirstSecond = first + second
    print(amountFirstSecond, end=' ')