int_n, int_k = map(int, input().split())
li_r = list(map(int, input().split()))

w = 0
for i in sorted(li_r)[-1 * int_k:]:
    w = (i + w) / 2

print(w)

