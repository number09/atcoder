n, k = map(int, input().split())

li_h = list()
for i in range(n):
    li_h.append(int(input()))

s_li_h = sorted(li_h)

wk = k - 1
li_diff = list()
for i in range(wk, n):
    li_diff.append(s_li_h[i] - s_li_h[i - wk])

print(min(li_diff))
