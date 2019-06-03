n = int(input())

sum = 0

for _ in range(n):
    sum += max(map(int, input().split()))

print(sum)