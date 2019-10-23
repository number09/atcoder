n = int(input())
li_a = map(int, input().split())
total = 1
kisuu = 1
for a in li_a:
    if a == 0:
        total *= 2
        kisuu *= 1
    else:
        total *= 3
        if a % 2 == 1:
            kisuu *= 1
        else:
            kisuu *= 2
print(total - kisuu)
