import math

n, a, b, c, d = map(int, input().split())

w_a = math.ceil(n / a)
w_c = math.ceil(n / c)

if w_a * b >= w_c * d:
    print(w_c * d)
else:
    print(w_a * b)

