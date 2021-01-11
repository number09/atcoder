x, y = map(int, input().split())

low, high = sorted([x, y])

if low + 3 > high:
    print('Yes')
else:
    print('No')