a, b, c = map(int, input().split())

answer = c - (a - b)
print(answer if answer > 0 else 0)