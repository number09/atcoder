a, b = map(int, input().split())

print(sum(list(sorted([a, a - 1, b, b - 1], reverse=True))[:2]))
