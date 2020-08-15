in_1 = ''
in_2 = ''
while True:
    w_in = input()
    if w_in == '0 0':
        exit(0)
    else:
        if not in_1:
            in_1 = w_in
        else:
            in_2 = w_in

    if in_1 and in_2:
        n, k = map(int, in_1.split())
        li_x = list(map(int, in_2.split()))
        print(sum(sorted(li_x)[:k]))
        in_1 = ''
        in_2 = ''
