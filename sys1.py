import sys
import os

def clear():
    os.system('CLS')

print(sys.argv, len(sys.argv))

def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.platform]:
        print("---->", i)

sa = sys.argv
if len(sa) < 2:
    clear()
    print_sys_vars()
    sys.exit()

with open(sa[1], "r", encoding='utf-8') as file:
    for line in file:
        print(line)

    