y, m, d = map(int, input().split())

if m == 12 and d == 25:
    print(y - 2018)
else:
    print("NOT CHRISTMAS DAY")
