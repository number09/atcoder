b = int(input())


for i in range(2, b):
    tmp = i
    li_w = list()
    li_w.append(i)

    while tmp <= b:
        tmp = int(tmp * 1.5)
        li_w.append(tmp)
        if tmp == b:
            print(len(li_w) - 1)
            exit(0)
else:
    print(0)
