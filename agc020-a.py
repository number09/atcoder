n, a, b = map(int, input().split())

diff = b - a
if diff % 2 == 0:
    print('Alice')
else:
    print('Borys')
