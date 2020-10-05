s = input()
joi = 0
ioi = 0
for i in range(len(s) - 2):
    w = s[i: i + 3]
    if w == 'JOI':
        joi += 1
    elif w == 'IOI':
        ioi += 1
print(joi)
print(ioi)
