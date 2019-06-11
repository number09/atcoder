n = int(input())

li_w = list(map(int, input().split()))

li_w_a = list()
li_w_b = list()

for l in li_w:
    if len(li_w_a) == 0:
        li_w_a.append(l)
    else:
        li_w_a.append(li_w_a[-1] + l)


for m in li_w[::-1]:
    if len(li_w_b) == 0:
        li_w_b.append(m)
    else:
        li_w_b.insert(0, li_w_b[0] + m)


w_min = max(li_w)
for idx in range(n - 1):
    w_min = min(w_min, abs(li_w_a[idx] - li_w_b[idx + 1]))
print(w_min)

