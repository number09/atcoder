n = int(input())
li_a = list(map(int, input().split()))
ln = len(li_a)
answer = 0
for s in range(ln):
    for e in range(s + 1, ln + 1):
        if sum(li_a[s:e]) == n:
            answer += 1
            break
        elif sum(li_a[s:e]) > n:
            break
print(answer)

