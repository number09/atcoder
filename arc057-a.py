a, k = map(int, input().split())

days = 0

if k == 0:
    days = 2 *(10**12) - a
else:
    while a < 2 * (10**12):
        a += (1 + k * a)
        days += 1

print(days)
