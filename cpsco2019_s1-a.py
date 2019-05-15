import math

n, a = map(int, input().split())

print(math.ceil(a / 3), (n // 3) if a >= (n // 3) else a)
