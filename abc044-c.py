from itertools import combinations

n, a = map(int, input().split())
li_x = list(map(int, input().split()))

counter = 0
for i in range(1, n + 1):
    for c in combinations(li_x, i):
        # print(c)
        if sum(c) == a * i:
            counter += 1

print(counter)
