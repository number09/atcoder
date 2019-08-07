import math

y = int(input())
m = int(input())
d = int(input())

if m == 1:
    y = y - 1
    m = 13
if m == 2:
    y = y - 1
    m = 14

def calc(i_y, i_m, i_d):
    answer = 365 * i_y + math.floor(i_y / 4) - math.floor(i_y / 100) + math.floor(i_y / 400) + math.floor((306 * (i_m + 1)) / 10) + i_d - 429

    return answer

print(calc(2014, 5, 17) - calc(y, m, d))

