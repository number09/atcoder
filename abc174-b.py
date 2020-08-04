import math

n, d = map(int, input().split())

li_p = []

for i in range(n):
    li_p.append(tuple(map(int, input().split())))

answer = 0
for x, y in li_p:
    if math.sqrt(x ** 2 + y ** 2) <= d:
        answer += 1
print(answer)
