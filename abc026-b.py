import math

n = int(input())
li_r = sorted([int(input()) for i in range(n)], reverse=True)

cir_r_red = [r ** 2 * math.pi for idx, r in enumerate(li_r, start=1) if idx % 2 == 1]
cir_r_white = [r ** 2 * math.pi for idx, r in enumerate(li_r, start=1) if idx % 2 == 0]

print(sum(cir_r_red) - sum(cir_r_white))



