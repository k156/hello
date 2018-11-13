from functools import reduce

lst =[1,2,3,4]
product = reduce(lambda x, y: x + y, lst)
print("porduct>>", product)

