n = int(input())
li_w = list()

for _ in range(n):
    li_w.append(input().split())

li_sorted = sorted(li_w, key=lambda x: (x[0], 100 - int(x[1])))
for a in li_sorted:
    print(li_w.index(a) + 1)

