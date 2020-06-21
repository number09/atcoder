a, b, n = map(int, input().split())
x = input()

for w in x:
    if w == 'S':
        a = max(a - 1, 0)
    elif w == 'C':
        b = max(b - 1, 0)
    else:
        if a >= b:
            a = max(a - 1, 0)
        else:
            b = max(b - 1, 0)
print(a)
print(b)

