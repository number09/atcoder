n, m = map(int, input().split())
li_cost = []
li_border = []
d_vote = {}
for _ in range(n):
    li_cost.append(int(input()))
for _ in range(m):
    li_border.append(int(input()))
for b in li_border:
    for idx, c in enumerate(li_cost):
        if b >= c:
            d_vote[idx + 1] = d_vote.get(idx + 1, 0) + 1
            break
print(sorted(d_vote.items(), key=lambda x: x[1], reverse=True)[0][0])

