l, x, y, s, d = map(int, input().split())

asc_dist = 0
desc_dist = 0

if s < d:
    asc_dist = d - s
    desc_dist = s + l - d
else:
    asc_dist = l - s + d
    desc_dist = s - d

if x < y:
    print(min(asc_dist / (x + y), desc_dist / (y - x)))
else:
    print(asc_dist / (x + y))


