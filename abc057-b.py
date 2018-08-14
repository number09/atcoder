int_n, int_m = map(int, input().split())

li_n = list()
li_m = list()

for i in range(int_n):
    li_n.append(list(map(int, input().split())))

for i in range(int_m):
    li_m.append(list(map(int, input().split())))


for n in li_n:
    l_dis = [abs(n[0] - m[0]) + abs(n[1] - m[1]) for m in li_m]

    minimum = min(l_dis)
    print(l_dis.index(minimum) + 1)




