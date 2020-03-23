n, m = map(int, input().split())
answer = 0
if n >= 2:
    answer += (n * (n - 1)) // 2
if m >= 2:
    answer += (m * (m - 1)) // 2
print(answer)
