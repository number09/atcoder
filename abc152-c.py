n = int(input())
li_p = list(map(int, input().split()))

answer = 0
mi = -1
for idx, p in enumerate(li_p):
    if idx == 0:
        mi = p
        answer += 1
    else:
        if p <= mi:
            answer += 1
        mi = min(mi, p)
print(answer)

