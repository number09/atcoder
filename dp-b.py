n, k = map(int, input().split())

li_h = list(map(int, input().split()))


dp = [float("inf")] * n

dp[0] = 0

for i in range(1, n):
    w = i - k if i - k > 0 else 0
    dp[i] = min([cost + abs(height - li_h[i]) for cost, height in zip(dp[w:i], li_h[w:i])])

print(dp[-1])

