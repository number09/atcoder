n, q = map(int, input().split())
s = input()
li_lr = list()

li_flg = [0] * len(s)

for i in range(q):
    li_lr.append(list(map(int, input().split())))


for idx, v in enumerate(s):
    if v == 'C' and idx != 0 and s[idx - 1] == 'A':
        li_flg[idx] = li_flg[idx - 1] + 1
    else:
        li_flg[idx] = li_flg[idx - 1]

for l in li_lr:
    print(li_flg[l[1] - 1] - li_flg[l[0] - 1])


