import math
a, b = input().split()

w = int(a + b)

if int(math.sqrt(w)) ** 2 == w:
    print("Yes")
else:
    print("No")
