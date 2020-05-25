a, b, c = map(int, input().split())
print(sum(sorted([a, b, c], reverse=True)[:2]))
