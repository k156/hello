i, sum = 3, 2
while (i < 100):
    isPrime = True

    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        sum = sum + i
    i = i + 1
            
print(sum)