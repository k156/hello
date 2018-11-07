i, sum = 1, 0
while (i < 100):
    for j in range (1, 100):
        if i > j and i % j != 0:
            sum = sum + i
    i += 1
print (sum)