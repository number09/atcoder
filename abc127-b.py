r, d, x = map(int, input().split())

result = x
for _ in range(10):
    result = r * result - d
    print(result)

