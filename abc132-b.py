n = int(input())

li_p = list(map(int, input().split()))
answer = 0
for i in range(1, n - 1):
    li_w = li_p[i - 1:i + 2]
    if sorted(li_w).index(li_p[i]) == 1:
        answer += 1

print(answer)

