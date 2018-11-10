a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

teika = b * t + a * s
waribiki = 0
if s + t >= k:
    waribiki = c * (s + t)

print(teika - waribiki)
