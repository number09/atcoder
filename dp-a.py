n = int(input())

li_h = list(map(int, input().split()))


li_cost = [float("inf")] * n

li_cost[0] = 0

# i = 現在の足場
for i in range(n):
    if i + 1 < n:
        li_cost[i + 1] = min(abs(li_h[i] - li_h[i + 1]) + li_cost[i], li_cost[i + 1])
    if i + 2 < n:
        li_cost[i + 2] = min(abs(li_h[i] - li_h[i + 2]) + li_cost[i], li_cost[i + 2])

print(li_cost[-1])

