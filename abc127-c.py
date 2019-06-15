n, m = map(int, input().split())

li_w = list()

for _ in range(m):
    li_w.append(tuple(map(int, input().split())))

w_l = 0
w_r = 999999

for w in li_w:
    w_l = max(w_l, w[0])
    w_r = min(w_r, w[1])


if w_r >= w_l:
    print(w_r - w_l + 1)
else:
    print(0)
