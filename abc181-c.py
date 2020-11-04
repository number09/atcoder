from itertools import combinations

n = int(input())
li_p = []

for _ in range(n):
    li_p.append(list(map(int, input().split())))

for p in combinations(li_p, 3):
    x1, y1 = p[1][0] - p[0][0], p[1][1] - p[0][1]
    x2, y2 = p[2][0] - p[0][0], p[2][1] - p[0][1]

    if y1 * x2 == y2 * x1:
        print('Yes')
        exit(0)
else:
    print('No')
