a, b, c, d = map(int, input().split())
li_s = []
for _ in range(c):
    li_s.append(list(map(int, input().split())))

li_border = []
for l in li_s:
    li_border.append(sorted(l, reverse=True)[b - 1])
print(sorted(li_border, reverse=True)[d - 1])