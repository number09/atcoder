n, x = map(int, input().split())

print(x - 1 if (x - 1) < (n - x) else n - x)
