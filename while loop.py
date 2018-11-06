i, sum = 0, 0
while (i >= 0):
    i += 1
    if ( i > 10 and i < 20):
        continue

    sum += i #i=10 sum= 10
    if (i == 100):
        print("End!!", sum)
        break