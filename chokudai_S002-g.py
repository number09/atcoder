# import math
import fractions
n = int(input())

li_w = list()

for _ in range(n):
    li_w.append(tuple(map(int, input().split())))

for l in li_w:
    # print(math.gcd(l[0], l[1]))
    print(fractions.gcd(l[0], l[1]))
