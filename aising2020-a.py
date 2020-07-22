l, r, d = map(int, input().split())
answer = 0
for i in range(l, r + 1):
    if i % d == 0:
        answer += 1
print(answer)
