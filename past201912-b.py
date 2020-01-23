n = int(input())
li_a = list()

for i in range(n):
    li_a.append(int(input()))
memo = 0

for idx, l in enumerate(li_a):
    if idx == 0:
        pass
    else:
        if memo > l:
            print('down {0}'.format(abs(memo - l)))
        elif memo < l:
            print('up {0}'.format(abs(memo - l)))
        else:
            print('stay')
    memo = l
