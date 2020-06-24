a, r, n = map(int, input().split())
ans = 0
if r == 1:
    ans = a
    print(ans)
else:
    if n >= 31:
        print('large')
    else:
        ans = a * (r ** (n - 1))
        if ans > 10 ** 9:
            print('large')
        else:
            print(ans)

