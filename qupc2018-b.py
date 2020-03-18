q = int(input())
li_in = list()

for i in range(q):
    li_in.append(list(map(int, input().split())))

for l in li_in:
    a, b, c = l
    goukei = 100 * a + 10 * b + c
    if goukei % 2 != 0:
        print('No')
        continue
    han = goukei // 2
    wk_a = min(han // 100, a)
    zan_a = han - (100 * wk_a)
    if zan_a == 0:
        print('Yes')
        continue
    wk_b = min(zan_a // 10, b)
    zan_b = zan_a - (10 * wk_b)
    if zan_b == 0:
        print('Yes')
        continue
    if zan_b <= c:
        print('Yes')
    else:
        print('No')



