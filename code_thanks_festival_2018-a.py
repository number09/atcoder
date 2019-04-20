t, a, b, c, d = map(int, input().split())

if t >= a + c:
    print(b + d)
elif t >= c:
    print(d)
elif t >= a:
    print(b)
else:
    print(0)