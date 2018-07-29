int_n, int_m = map(int, input().split())

roads = dict()

for i in range(int_m):
    road = tuple(map(int, input().split()))

    for r in road:
        if r in roads:
            roads[r] += 1
        else:
            roads[r] = 1


for i in sorted(roads):
    print(roads[i])




