n, s, t = map(int, input().split())
li_w = list()
li_w.append(int(input()))

for i in range(n - 1):
    li_w.append(li_w[-1] + int(input()))

print(len(list(filter(lambda x: s <= x <= t, li_w))))


