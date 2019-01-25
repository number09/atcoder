import math

txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
li_g = list()
for i in range(n):
    li_g.append(list(map(int, input().split())))


for g in li_g:
    length = math.sqrt((g[0] - txa) ** 2 + (g[1] - tya) ** 2) + math.sqrt((txb - g[0]) ** 2 + (tyb - g[1]) ** 2)
    if length <= (t * v):
        print("YES")
        break
else:
    print("NO")



