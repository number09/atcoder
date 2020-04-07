s, l, r = map(int, input().split())

if l <= s <= r:
    print(s)
elif abs(l - s) <= abs(r - s):
    print(l)
else:
    print(r)
