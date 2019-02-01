n, m = map(int, input().split())
li_score = [0] * (m + 1)

total = 0
for i in range(n):
    tmp = list(map(int, input().split()))

    li_score[tmp[0] - 1] += tmp[2]
    li_score[tmp[1]] -= tmp[2]
    total += tmp[2]


for i in range(1, len(li_score)):
    li_score[i] += li_score[i - 1]

print(total - min(li_score[:-1]))




