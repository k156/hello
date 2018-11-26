import re

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
Although that way may not be obvious at first unless you're Dutch
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


is_better = re.findall("(.*)is .*better than(.*)", zen, re.MULTILINE)

print(is_better)

for i in is_better:
    string = "{} > {}"
    d = string.format(i[0].lower(),i[1].strip('.'))
    print(d)
00     

# better_list = ['Beautiful is better than ugly.', 'Explicit is better than implicit.', 'Simple is better than complex.', 'Complex is better than complicated.', 'Flat is better than nested.', 'Sparse is better than dense.', 'Now is better than never.']

# for i in better_list:
#     i.strip('')
#     print(i)


# b = """
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Now is better than never."""



# better = re.findall("(.*)is better than(.*)", b, re.MULTILINE)

# print(better)


# b_list = [('Beautiful ', ' ugly.'), ('Explicit ', ' implicit.'), ('Simple ', ' complex.'), ('Complex ', ' complicated.'), ('Flat ', ' nested.'), ('Sparse ', 'dense.'), ('Now ', ' never.')]

# for i in b_list:
#     string = "{} > {}"
#     d = string.format(i[0].lower(),i[1].strip('.'))
#     print(d)
