a, b, k, l = map(int, input().split())
print(
    ((k // l) * b) + min((k % l) * a, b)
)