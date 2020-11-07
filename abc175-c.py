x, k, d = map(int, input().split())

abs_min = abs(x)

num = abs(x // d)

if num > k:
    print(min(abs(x - (d * k)), abs(x + (d * k))))
else:
    k = k - num
    now = min(abs(x - (d * num)), abs(x + (d * num)))
    if k % 2 == 0:
        print(now)
    else:
        print(min(abs(now + d), abs(now - d)))



