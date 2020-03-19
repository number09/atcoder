s = input()
doremi = 'WBWBWWBWBWBW' * 2


for i in range(12):
    wk = doremi[i:20]
    if all([x == y for x, y in zip(wk, s)]):
        if i == 0:
            print('Do')
            exit(0)
        elif i == 2:
            print('Re')
            exit(0)
        elif i == 4:
            print('Mi')
            exit(0)
        elif i == 5:
            print('Fa')
            exit(0)
        elif i == 7:
            print('So')
            exit(0)
        elif i == 9:
            print('La')
            exit(0)
        elif i == 11:
            print('Si')
            exit(0)

