n = int(input())

li_height = list(map(int, input().split()))

li_cost = [99999 ** 10] * n
li_cost[0] = 0

for from_index in range(n):
    to_1 = from_index + 1
    if to_1 <= (n - 1):
        cost = abs(li_height[from_index] - li_height[to_1]) + li_cost[from_index]
        li_cost[to_1] = min(li_cost[to_1], cost)

    to_2 = from_index + 2
    if to_2 <= (n - 1):
        cost = abs(li_height[from_index] - li_height[to_2]) + li_cost[from_index]
        li_cost[to_2] = min(li_cost[to_2], cost)

print(li_cost[-1])



