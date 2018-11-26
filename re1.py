import re
line = "Beautiful is better than ugly."

matches = re.findall("Beautiful", line)

print(matches)

matches2 = re.findall("beautiful", line, re.IGNORECASE)

print(matches2)


zen2 = """Although never is often better than * right * now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea - - let's do more of those!"""


m = re.findall("^If", zen2, re.MULTILINE)
m2 =  re.findall("idea\.", zen2, re.MULTILINE)
m22 = re.findall("idea.", zen2, re.MULTILINE)
m3 = re.findall("idea.$", zen2, re.MULTILINE)
print(m, m2, m22, m3)

string = "Two aa too"

m4 = re.findall("t[ow]o", string)
m5 = re.findall("t[ow]o", string, re.IGNORECASE)
print(m4, m5)

m6 = re.findall("t[^w]o",string, re.IGNORECASE)
print(m6)

string2 = "123?45yy7890 hi 999 hello"

m7 = re.findall("\d", string2)
m8 = re.findall("[0-9]{1,2}", string2)
m9 = re.findall("[1-5]{1,2}", string2)
a1 = re.findall("[A-z]", string2)

print("m7>>",m7)
print("m8>>",m8)
print("m9>>",m9)
print(a1)