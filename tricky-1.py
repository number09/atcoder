import sys

n = int(sys.stdin.buffer.readline())

for i in range(n):
    x, y = map(int, sys.stdin.buffer.readline().split())

    if x < 0 <= y:
        print(-(-x // y))
    elif x >= 0 > y:
        print(-(x // -y))
    else:
        print(x // y)
