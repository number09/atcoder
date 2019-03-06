int_n, int_k = map(int, input().split())

li_wk = list()

for i in range(int_n):
    li_wk.append(list(map(int, input().split())))

li_wk.sort(key=lambda x: x[0])

counter = 1
for l in li_wk:
    if counter <= int_k <= (counter + l[1] - 1):
        print(l[0])
    counter += l[1]




