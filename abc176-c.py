n = int(input())
li_a = list(map(int, input().split()))

answer = 0
prev = 0
for idx, v in enumerate(li_a):
    if idx == 0:
        prev = v

    if prev > v:
        answer += (prev - v)
    else:
        prev = v
print(answer)
