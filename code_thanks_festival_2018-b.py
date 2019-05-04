x, y = map(int, input().split())


if (x + y) % 4 != 0:
    print("No")
else:
    w = (x + y) // 4
    if x - w >= 0 and (x - w) % 2 == 0 and y - w >= 0 and (y - w) % 2 == 0:
        print("Yes")
    else:
        print("No")
