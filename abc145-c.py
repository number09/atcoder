from itertools import combinations
import math
n = int(input())
li_point = list()
li_kyori = list()
for i in range(n):
    li_point.append(list(map(int, input().split())))


for x, y in combinations(range(n), 2):
    li_kyori.append(
        math.sqrt(
            abs(li_point[x][0] - li_point[y][0]) ** 2 +
            abs(li_point[x][1] - li_point[y][1]) ** 2
        )
    )

ave = sum(li_kyori) / len(li_kyori)
print(ave * (n - 1))
