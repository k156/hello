samples = [
    (2001, 23),
    (2002, 7),
    (2002, -12),
    (2001, 21),
    (2003, 20),
    (2005, 13),
    (2003, 3),
    (2005, -2),
    (2003, 22),
    (2001, -3),
]





dic = sorted(samples, key = lambda d: d[0])

print(dic)


dic2 = {}



for d in dic:
    dic2[d[0]] = []
    dic2[d[0]].append(d[1])
print(dic2)
