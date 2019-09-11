import re
s = input()
pattern = '(\d+)'
num = re.findall(pattern, s)[0]

print(num)


