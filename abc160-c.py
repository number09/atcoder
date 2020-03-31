k, n = map(int, input().split())
li_a = list(map(int, input().split()))
li_d = list()
for idx, a in enumerate(li_a):
    if idx == (n - 1):
        li_d.append(abs(k - li_a[idx] + li_a[0]))
    else:
        li_d.append(abs(li_a[idx] - li_a[idx + 1]))
print(sum(li_d) - max(li_d))
