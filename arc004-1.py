from math import sqrt
from itertools import combinations
n = int(input())
li_point = list()
answer = 0
for _ in range(n):
    li_point.append(tuple(map(int, input().split())))


for p1, p2 in combinations(li_point, 2):
    answer = max(answer, sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))

print(answer)
