n = int(input())
li_histroy = list()
li_w = list()
for i in range(n):
    li_w.append(input())

for idx, val in enumerate(li_w):
    if len(li_histroy) == 0:
        pass
    else:
        if val in li_histroy or li_histroy[-1][-1] != val[0]:
            if idx % 2 == 0:
                print('LOSE')
                exit(0)
            else:
                print('WIN')
                exit(0)
        else:
            pass
    li_histroy.append(val)
else:
    print('DRAW')