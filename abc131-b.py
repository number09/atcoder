n, l = map(int, input().split())

eats = 999
is_minus = False

for i in range(n):
    azi = l + (i + 1) - 1

    if eats > abs(azi):
        eats = abs(azi)
        is_minus = True if azi < 0 else False


w = eats if is_minus == False else eats * -1

print(sum([l + (e + 1) - 1 for e in range(n)]) - w)

