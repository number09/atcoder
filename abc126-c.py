n, k = map(int, input().split())

answer = 0

for i in range(1, n + 1):
    score = i
    coin = 0
    while 1 <= score <= k - 1:
        score = score * 2
        coin += 1

    answer += (1 / n) * (0.5 ** coin)

print(answer)
