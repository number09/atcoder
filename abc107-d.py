int_n = int(input())
li_a = list(map(int, input().split()))


def cyuoh(target):
    sorted_target = sorted(target)
    idx = (len(target) // 2 + 1) - 1
    return sorted_target[idx]


# 連続部分列の列挙
li_m = list()

for l in range(int_n + 1):
    for r in range(l + 1, int_n + 1):
        li_m.append(cyuoh(li_a[l:r]))


print(cyuoh(li_m))



