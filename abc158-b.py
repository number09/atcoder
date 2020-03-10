n, a, b = map(int, input().split())

w = n // (a + b)
m = n % (a + b)
if m >= a:
    print(w * a + a)
else:
    print(w * a + m)

