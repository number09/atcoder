x, n = map(int, input().split())
li_p = list(map(int, input().split()))

answer = -1
for i in range(max(x - n, 0), x + n + 1):
    if i in li_p:
        continue
    if abs(answer - x) > abs(i - x):
        answer = i
print(answer)
