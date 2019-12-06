n, k = map(int, input().split())
li_a = list(map(int, input().split()))
sum = 0
for idx, w in enumerate(sorted(li_a, reverse=True)):
    sum += w
    if sum >= k:
        print(idx + 1)
        exit(0)
else:
    print(-1)
