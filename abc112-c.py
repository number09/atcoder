n = int(input())

li_input = list()

for i in range(n):
    li_input.append(tuple(map(int, input().split())))


for x in range(101):
    for y in range(101):
        set_H = set()
        for ipt in li_input:
            set_H.add(ipt[2] + abs(x - ipt[0]) + abs(y - ipt[1]))
        if len(set_H) == 1:
            print(x, y, set_H.pop())
