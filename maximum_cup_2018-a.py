n = int(input())

answer = 0

for i in range(n):
    t, d, m = map(int, input().split())
    if t + 10 <= d:
        answer += m
print(answer)
