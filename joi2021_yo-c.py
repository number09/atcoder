n, m = map(int, input().split())
se_a = set(map(int,input().split()))
se_b = set(map(int, input().split()))

w_se = se_a.intersection(se_b)
for s in sorted(w_se):
    print(s)

