import math

n = int(input())
di = dict()
answer = 0

for i in range(n):
    tmp = str(sorted(input()))
    if di.get(tmp, 0) == 0:
        di[tmp] = 1
    else:
        answer += di[tmp]
        di[tmp] += 1

print(answer)


