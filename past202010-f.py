n, k = map(int, input().split())

d_s = dict()
for _ in range(n):
    w = input()
    d_s[w] = d_s.get(w, 0) + 1

nums = sorted(list(d_s.values()), reverse=True)

wn = nums[k - 1]

li_an = []
for key, val in d_s.items():
    if val == wn:
        li_an.append(key)
if len(li_an) > 1:
    print('AMBIGUOUS')
else:
    print(li_an[0])