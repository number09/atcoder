n, x = map(int, input().split())
li_a = list(map(int, input().split()))

m = max(li_a)
print(len(list(filter(lambda y: m - y <= x, li_a))))
