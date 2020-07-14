n, k = map(int, input().split())

answer = 0
total = 0
for i in range(n):
    total += int(input())
    if total >= k and answer == 0:
        answer = i + 1
print(answer)
