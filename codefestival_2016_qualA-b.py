n = int(input())
li_a = list(map(int, input().split()))
answer = 0
for idx, a in enumerate(li_a):
    if li_a[a-1] == idx + 1:
        answer += 1
print(int(answer / 2))
