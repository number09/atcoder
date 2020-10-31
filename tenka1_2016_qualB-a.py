import math


def fun(n):
    return math.floor(((n ** 2) + 4) / 8)

print(fun(fun(fun(20))))