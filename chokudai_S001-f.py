n = int(input())
li_a = list(map(int, input().split()))

mi = 0
answer = 0
for idx, l in enumerate(li_a):
    if idx == 0:
        ma = l
        answer += 1
    else:
        if l > ma:
            answer += 1
            ma = max(ma, l)
print(answer)
