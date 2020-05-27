x, l, r = map(int, input().split())

if l <= x <= r:
    print(x)
else:
    if x < l:
        print(l)
    else:
        print(r)
