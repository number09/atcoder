n, x = map(int, input().split())

li_w = list()
max_b = 0
max_b_idx = 999
for i in range(n):
    a, b = map(int, input().split())
    if max_b < b:
        max_b = b
        max_b_idx = i
    li_w.append([a, b])


if max_b_idx != 999:
    li_w[max_b_idx][0] = li_w[max_b_idx][0] + x

print(sum([l[0] * l[1] for l in li_w]))
