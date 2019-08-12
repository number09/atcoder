h, m = map(int, input().split())

d_h = 18 - h - 1

d_m = 60 - m

print(d_h * 60 + d_m)

