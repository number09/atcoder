import math
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

d_a = math.ceil(a / c)
d_b = math.ceil(b / d)

print(l - max(d_a, d_b))
