n, k = map(int, input().split())
li_h = list(map(int, input().split()))

print(sum(sorted(li_h, reverse=True)[k:]))
