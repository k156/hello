import random
from pprint import pprint
data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

# pprint(data)


def add(table):
	sum1 = 0
	for n in range(0,5):
		sum1 += data[table][n][n]
	
	sum2 = 0
	sort = sorted(range(0,5), reverse = True)
	
	for i, m in enumerate(sort):
		sum2 += data[table][i][m]

	print(sum1+sum2)








# def add(table):
# 	sum1 = 0
# 	for n in range(0,5):
# 		sum1 += data[table][n][n]
	
# 	sum2 = 0
# 	sort = sorted(range(0,5), reverse = True)
	
# 	for i, m in enumerate(sort):
# 		sum2 += data[table][i][m]

# 	print(sum1+sum2)


# add('A') 
# add('B') 
# add('C')




# sum1 = 0
# for n in range(0,5):
# 	sum1 += data['A'][n][n]
# # print(sum1)

# sum2 = 0

# sort = sorted(range(0,5), reverse = True)

# for i, m in enumerate(sort):
# 	sum2 += data['A'][i][m]
# # print(sum2)

# print(sum1+sum2)


