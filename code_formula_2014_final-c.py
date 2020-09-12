import re
s = input()

user = set()
r = re.compile(r'@([a-z]+)')

for l in s.split():
    res = re.findall(r, l)
    if res:
        for w in res:
            user.add(w)
for u in sorted(user):
    print(u)