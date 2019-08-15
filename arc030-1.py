import math
n = int(input())
k = int(input())

if math.ceil((n - 1) / 2) >= k:
    print("YES")
else:
    print("NO")

