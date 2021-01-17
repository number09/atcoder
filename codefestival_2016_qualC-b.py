k, t = map(int, input().split())
li_a = list(map(int, input().split()))

max_a = max(li_a)

print(max(max_a - 1 - (k - max_a), 0))