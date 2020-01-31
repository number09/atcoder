n, k = map(int, input().split())
li_a = list(map(int, input().split()))

print(sum(sorted(li_a)[:k]) + sum(range(k)))
