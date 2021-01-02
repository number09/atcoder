import re

n = int(input())
li_s = []
for _ in range(n):
    li_s.append(input())

for i in sorted(li_s, key=lambda x: (int(x), -1 * len(re.match(r'^(0*).*$', x).groups()[0]))):
    print(i)
