int_x = int(input())

li_dist = list()
for i in range(1, int_x + 1):
    if len(li_dist) == 0:
        li_dist = [i, -i, 0]
    else:
        li_dist = [x + y for x in [i, -i, 0] for y in li_dist]

    if int_x in li_dist:
        print(i)
        exit(0)


