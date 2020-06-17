n = int(input())

mi = 1 * n
ma = 6 * n

len = ma - mi + 1

if n == 1:
    print(1)
elif len % 2 == 0:
    idx = (len // 2) - 1
    print(mi + idx)
else:
    idx = (len // 2)
    print(mi + idx)
