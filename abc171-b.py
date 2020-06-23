n, k = map(int, input().split())
li_p = list(map(int, input().split()))

print(sum(sorted(li_p)[:k]))
