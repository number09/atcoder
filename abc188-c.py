n = int(input())
li_a = list(map(int, input().split()))

max_a = max(li_a)
max_idx = li_a.index(max_a)
half = int((len(li_a)/2) - 1)
if half >= max_idx:
    semi_win = max(li_a[half + 1:])
else:
    semi_win = max(li_a[:half + 1])
print(li_a.index(semi_win) + 1)
