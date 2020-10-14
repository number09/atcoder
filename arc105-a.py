from itertools import combinations
a, b, c, d = map(int, input().split())

su = sum([a, b, c, d])

li = sorted([a, b, c, d])
for i in range(1, 4):
    for c in combinations(li, i):
        w_sum = sum([int(w) for w in c])
        if su - w_sum == w_sum:
            print('Yes')
            exit(0)
else:
    print('No')
