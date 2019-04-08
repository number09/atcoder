a, b, c = map(int, input().split())

counter = 0

li_wk = sorted([a, b, c], reverse=True)

if (li_wk[0] - li_wk[1]) >= 2:
    add_1 = (li_wk[0] - li_wk[1]) // 2
    li_wk[1] += (add_1 * 2)
    counter += add_1

if (li_wk[0] - li_wk[2]) >= 2:
    add_2 = (li_wk[0] - li_wk[2]) // 2
    li_wk[2] += (add_2 * 2)
    counter += add_2

if li_wk.count(li_wk[0]) == 3:
    pass
elif li_wk.count(li_wk[0]) == 2:
    counter += 2
else:
    counter += 1

print(counter)




