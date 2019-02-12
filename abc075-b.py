int_h, int_w = map(int, input().split())
l_h = list()
for i in range(int_h):
    l_h.append(input())

l_temp = list()
l_temp.append(list(map(int, "0" * (int_w + 2))))
for r in l_h:
    l_temp.append(list(map(lambda x: int(x) if x != "#" else x, "0" + r.replace(".", "0") + "0")))

l_temp.append(list(map(int, "0" * (int_w + 2))))


# print(l_temp)


for rownum, row in enumerate(l_temp):
    for colnum, col in enumerate(row):
        if col == "#":
            for c in [-1, 0, 1]:
                if l_temp[rownum - 1][colnum + c] != "#":
                    l_temp[rownum - 1][colnum + c] += 1
                if l_temp[rownum + 1][colnum + c] != "#":
                    l_temp[rownum + 1][colnum + c] += 1
            for c in [-1, 1]:
                if l_temp[rownum][colnum + c] != "#":
                    l_temp[rownum][colnum + c] += 1


for row in l_temp[1:-1]:
    print("".join(map(str,row[1:-1])))
