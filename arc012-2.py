n, a, b, l = map(int, input().split())

dist_a = 0
dist_b = l

for i in range(n):
    w_sec = l / a
    l = w_sec * b
    dist_b += l
    dist_a += w_sec * a
print(abs(dist_a - dist_b))
