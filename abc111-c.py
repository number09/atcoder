from collections import defaultdict

n = int(input())
li_input = list(map(int, input().split()))

li_ki = li_input[0::2]
d_ki = defaultdict(int)
for ki in li_ki:
    d_ki[ki] += 1


li_gu = li_input[1::2]
d_gu = defaultdict(int)
for gu in li_gu:
    d_gu[gu] += 1

ki_sort = sorted([(k, v) for k,v in d_ki.items()], key=lambda x : x[1], reverse=True)
gu_sort = sorted([(k, v) for k,v in d_gu.items()], key=lambda x : x[1], reverse=True)

ki_cnt = 0
gu_cnt = 0

if ki_sort[0][0] != gu_sort[0][0]:
    print(n - ki_sort[0][1] - gu_sort[0][1])
else:
    ki_1 = ki_sort[0][1]
    ki_2 = ki_sort[1][1] if len(ki_sort) > 1 else 0

    gu_1 = gu_sort[0][1]
    gu_2 = gu_sort[1][1] if len(gu_sort) > 1 else 0

    print(min(n - ki_1 - gu_2, n - ki_2 - gu_1))


