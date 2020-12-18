s = input()
li_list = []


def get_list_idx(firstword):
    for idx, lis in enumerate(li_list):
        if lis[0] == firstword and (
                (firstword == '5' and len(lis) % 2 != 0)
                or
                (firstword == '2' and len(lis) % 2 == 0)
        ):
            return idx
    else:
        li_list.append([])
        return len(li_list) - 1


for w in s[::-1]:
    if w == '2':
        idx_num = get_list_idx('5')
    else:
        idx_num = get_list_idx('2')
    li_list[idx_num] = [w] + li_list[idx_num]
if len([l for l in li_list if len(l) % 2 != 0]) > 0:
    print(-1)
    exit(0)
print(len(li_list))
