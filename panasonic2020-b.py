import math
h, w = map(int, input().split())
if h != 1 and w != 1:
    print(math.ceil((h * w) / 2))
else:
    print(1)


