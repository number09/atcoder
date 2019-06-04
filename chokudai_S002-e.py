n = int(input())

counter = 0

for _ in range(n):
    a, b = map(int, input().split())

    counter += min(a // 2, b)

print(counter)