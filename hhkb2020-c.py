n = int(input())
li_p = list(map(int, input().split()))

wk_set = set()
neq_min = 0
for p in li_p:
    wk_set.add(p)
    if neq_min != p:
        print(neq_min)
    else:
        while True:
            neq_min += 1
            if neq_min not in wk_set:
                break
        print(neq_min)

