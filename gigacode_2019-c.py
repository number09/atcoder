d = int(input())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))
li_a_sum = list()
for a in li_a:
    if len(li_a_sum) == 0:
        li_a_sum.append(a)
    else:
        li_a_sum.append(li_a_sum[-1] + a)

ok_list = list(filter(lambda x: x[0] >= x[1], zip(li_a_sum, li_b)))

if len(ok_list) == 0:
    print(-1)
else:
    print(sorted(ok_list, key=lambda x: x[1],)[0][1])
