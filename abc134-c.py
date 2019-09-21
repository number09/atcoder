n = int(input())
li_a = list()
d_a = dict()

for _ in range(n):
    wk = int(input())
    li_a.append(wk)

    get = d_a.get(wk, 0)
    d_a[wk] = get + 1

li_top2 = sorted(d_a.keys(), reverse=True)[:2]

for i in range(n):
    val = li_a[i]

    if val not in li_top2:
        print(li_top2[0])
    else:
        if val == li_top2[0] and d_a.get(val, 0) == 1:
            print(li_top2[1])
        else:
            print(li_top2[0])
