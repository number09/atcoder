n, m = map(int, input().split())

li_route = list()

for i in range(m):
    li_route.append(list(map(int, input().split())))

starts = set(l[1] for l in li_route if l[0] == 1)

ends = set(l[0] for l in li_route if l[1] == n)

if len(starts.intersection(ends)) > 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

