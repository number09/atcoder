n, m = map(int, input().split())
li_a = list(map(int, input().split()))

if sum(li_a) <= n:
    print(n - sum(li_a))
else:
    print(-1)

