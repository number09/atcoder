import re

s = input()

if re.search(r'o{3,}', s):
    print('o')
elif re.search(r'x{3,}', s):
    print('x')
else:
    print('draw')
