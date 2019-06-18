n, d = map(int, input().split())

li_a = list(map(int, input().split()))

if d == 1:
    print(sum(li_a))
elif n == d:
    print(min(li_a))
else:
    print(sum([sorted(li_a, reverse=True)[i] for i in range(d - 1, n, d)]))