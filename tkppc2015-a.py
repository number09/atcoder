n = int(input())

li_ab = list()

for i in range(n):
    li_ab.append(list(map(int, input().split())))

for l in li_ab:
    print(l[0] + l[1])
