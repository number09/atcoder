n, t = map(int, input().split())

li_a = list(map(int, input().split()))

i_div = 1
for i in range(n):
    if i == (n - 1):
        break
    else:
        if li_a[i] > li_a[i + 1]:
            i_div += 1

print((i_div - 1) * t + li_a[-1])
