a, b, m = map(int, input().split())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

wk = -1
for i in range(m):
    x, y, c = map(int, input().split())
    if wk == -1:
        wk = li_a[x - 1] + li_b[y - 1] - c
    else:
        wk = min(wk,li_a[x - 1] + li_b[y - 1] - c)
answer = min(wk,min(li_a) + min(li_b))
print(answer)
