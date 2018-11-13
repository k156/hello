int_numbers =  range(-5, 6)

positives = filter(lambda x: x > 0, int_numbers)
print(list(positives))

def fn(x):
    return x > 0

even_num = filter(lambda x: x >0 and x % 2 == 0, int_numbers)
print(list(even_num))

def fn(x):
    return x % 2 == 0


def make_double(x):
    return x * 3

triple_num = map(make_double, int_numbers)
print(list(triple_num))

double_num = map(lambda x: x *2, int_numbers)
print(list(double_num))

