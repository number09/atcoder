from itertools import combinations

n = int(input())

li_pair = []

for _ in range(n):
    li_pair.append(list(map(int, input().split())))

ans = 0
for c in combinations(li_pair, 2):
    w1 = c[0]
    w2 = c[1]
    if -1 <= ((w1[1] - w2[1]) / (w1[0] - w2[0])) <= 1:
        ans += 1
print(ans)


