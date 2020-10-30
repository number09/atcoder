x, y = map(int, input().split())

if y % 2 != 0 or y < 0:
    print(-1)
    exit(0)
w = y // 2

if abs(x) > abs(w):
    print(-1)
    exit(0)
if (abs(w) - abs(x)) % 2 != 0:
    print(-1)
    exit(0)

print(abs(w))
