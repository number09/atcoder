import math
x = int(input())
a = 100
answer = 0

while a < x:
    a += math.floor(a * 0.01)
    answer += 1
print(answer)
