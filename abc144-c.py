import math
n = int(input())
answer = n
for x in range(1, math.ceil(math.sqrt(n) + 1)):
    if n % x == 0:
        y = n // x
        answer = min(answer, x + y - 2)
print(answer)
