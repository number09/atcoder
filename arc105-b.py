import math
from functools import reduce

n = int(input())
li_a = list(map(int, input().split()))

print(reduce(math.gcd, li_a))

