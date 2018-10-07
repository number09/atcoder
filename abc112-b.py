n, t = map(int, input().split())

li_keiro = list()
for i in range(n):
    li_keiro.append(tuple(map(int, input().split())))

time_list = list(filter(lambda x: x[1] <= t, li_keiro))

if len(time_list) == 0:
    print("TLE")
else:
    print(min(time_list, key=lambda x: x[0])[0])
