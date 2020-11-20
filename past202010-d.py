n = int(input())
s = input()

x = 0
y = 0
li_s = s.split('#')


if s[0] == '.':
    x += len(li_s[0])
    li_s = li_s[1:]

if s[-1] == '.':
    y += len(li_s[-1])
    li_s = li_s[:-1]

if len(li_s) == 0 or max(map(len, li_s)) == 0:
    print(x, y)
else:
    w = max(map(len, li_s))
    if (x + y) >= w:
        print(x, y)
    else:
        print(x + (w - (x + y)), y)
