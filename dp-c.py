n = int(input())

li_action = list()

for _ in range(n):
    li_action.append(list(map(int, input().split())))

dp = list()
for _ in range(n):
    dp.append([0] * 3)


dp[0][0] = li_action[0][0]
dp[0][1] = li_action[0][1]
dp[0][2] = li_action[0][2]


for i in range(1, n):
    dp[i][0] = max(
        dp[i - 1][1] + li_action[i][0],
        dp[i - 1][2] + li_action[i][0],
    )
    dp[i][1] = max(
        dp[i - 1][0] + li_action[i][1],
        dp[i - 1][2] + li_action[i][1],
    )
    dp[i][2] = max(
        dp[i - 1][0] + li_action[i][2],
        dp[i - 1][1] + li_action[i][2],
    )
print(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))

