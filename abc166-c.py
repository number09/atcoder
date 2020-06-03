n, m = map(int, input().split())
li_h = list(map(int, input().split()))
li_route = list()
remove_idx_set = set()

for _ in range(m):
    a, b = map(int, input().split())

    h_a = li_h[a - 1]
    h_b = li_h[b - 1]

    if h_a <= h_b:
        remove_idx_set.add(a - 1)
    if h_a >= h_b:
        remove_idx_set.add(b - 1)
for s in remove_idx_set:
    li_h[s] = 0
print(len([v for v in li_h if v != 0]))
