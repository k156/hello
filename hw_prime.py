i, sum = 3, 2
while (i < 100):
    for j in range (2, i):
        if i % j == 0:
            break
        if j == (i - 1):
            sum = sum + i
    i += 1
print (sum)