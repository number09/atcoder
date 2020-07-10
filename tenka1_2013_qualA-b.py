n = int(input())
answer = 0
for _ in range(n):
    li_w = list(map(int, input().split()))
    if 0 <= sum(li_w) < 20:
        answer += 1
print(answer)
