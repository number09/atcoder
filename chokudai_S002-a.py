n = int(input())

li_w = list()

for _ in range(n):
    li_w.append(list(map(int, input().split())))

for l in li_w:
    print(l[0] * l[1])
