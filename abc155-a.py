a, b, c = map(int, input().split())

if len({a, b, c}) == 2:
    print('Yes')
else:
    print('No')
