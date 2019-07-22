import math
n = int(input())
answer = 0
for _ in range(n):
    item, price = map(int, input().split())
    answer += item * price

answer = math.floor(answer * 1.05)
print(answer)