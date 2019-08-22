n = int(input())

answer = 0
for i in range(n):
    li_w = list(map(int, input().split()))
    answer = max(answer, sum(li_w[:4]) + (li_w[4] * 110 / 900))

print(answer)