a, b, c = map(int, input().split())

tmp = a if a <= b else b

print(c // tmp)
