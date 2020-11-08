n, m = map(int, input().split())
li_a = []

for _ in range(m):
    li_a.append(int(input()))

th = list(range(1, n + 1))

for a in li_a:

    idx = th.index(a)
    v = th.pop(idx)
    th = [v] + th
for t in th:
    print(t)