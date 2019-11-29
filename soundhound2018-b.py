n, l, r = map(int, input().split())
li_a = list(map(int, input().split()))


def fn(a):
    if a < l:
        return l
    elif a > r:
        return r
    else:
        return a

print(" ".join(list(map(str, map(fn, li_a)))))
