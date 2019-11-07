import math
a, b, c = map(int, input().split())

day = 0
week = c // (a * 7 + b)
zan = c % (a * 7 + b)

if (a * 6) < zan:
    week += 1
else:
    day = math.ceil(zan / a)

print(week * 7 + day)
