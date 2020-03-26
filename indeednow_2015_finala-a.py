n = int(input())
li_a = list(map(int, input().split()))

li_w = sorted(li_a)
mx = 0
mn = sum(li_w)
for x, y in zip(li_w, li_w[::-1]):
    mx = max(mx, x + y)
    mn = min(mn, x + y)
print(mx - mn)
