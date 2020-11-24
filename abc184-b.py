n, x = map(int, input().split())
s = input()

for w in s:
    if w == 'o':
        x += 1
    else:
        x = max(x - 1, 0)
print(x)
