n, k, m = map(int, input().split())
li_a = list(map(int, input().split()))

target = (n * m) - sum(li_a)

if target > k:
    print(-1)
else:
    if target < 0:
        print(0)
    else:
        print(target)
