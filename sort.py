numbers = [5,4,3,2,1]
sort_num = sorted(numbers)
print("sort_numbers=", sort_num)
print("numbers=", numbers)

numbers.sort()
print("asc>>", numbers)

numbers.sort(reverse=True)
print("desc>>", numbers)

names = ["김정민", "김나온", "김남윤"]
names.sort()
print(names)