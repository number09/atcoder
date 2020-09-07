n = int(input())
li_a = list(map(int, input().split()))
li_in = []

for _ in range(n):
    li_in.append(input())

li_needs = []
for i in range(7):
    li_w = []
    for input in li_in:
        li_w.append(input[i])
    wk_li = "".join(li_w).split('-')
    li_needs.append(max([len(wk) for wk in wk_li]))
li_needs += [0, 0, 0]

for needs, finger in zip(sorted(li_needs, reverse=True), sorted(li_a, reverse=True)):
    if needs > finger:
        print('NO')
        exit(0)
else:
    print('YES')



