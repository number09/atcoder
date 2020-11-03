n = int(input())
li_ab = []
for _ in range(n):
    li_ab.append(list(map(int, input().split())))
answer = 0
for ab in li_ab:
    num = ab[1] - ab[0] + 1
    if num % 2 == 0:
        answer += (ab[1] + ab[0]) * (num // 2)
    else:
        answer += (ab[1] - 1 + ab[0]) * ((num - 1) // 2) + ab[1]
print(answer)