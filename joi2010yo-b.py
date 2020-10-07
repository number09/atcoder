n, m = map(int, input().split())
li_n = []
li_m = []
for _ in range(n):
    li_n.append(int(input()))
for _ in range(m):
    li_m.append(int(input()))

idx = 0
goal_idx = n - 1

for num, m in enumerate(li_m):
    idx += m
    if idx >= goal_idx:
        print(num + 1)
        exit(0)
    idx += li_n[idx]
    if idx >= goal_idx:
        print(num + 1)
        exit(0)
