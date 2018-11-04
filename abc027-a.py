li_l = list(map(int, input().split()))

for l in li_l:
    if li_l.count(l) == 1 or li_l.count(l) == 3:
        print(l)
        break


