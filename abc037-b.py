n, q = map(int, input().split())

li = [0] * n

w_li = li[:]

for i in range(q):
    left, right, t = map(int, input().split())
    w_li = [t if left <= idx <= right else item for idx, item in enumerate(w_li, 1)]

for w in w_li:
    print(w)


