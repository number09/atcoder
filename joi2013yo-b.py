n = int(input())
li_1 = list()
li_2 = list()
li_3 = list()

for i in range(n):
    a, b, c = map(int, input().split())
    li_1.append(a)
    li_2.append(b)
    li_3.append(c)

for li_0 in [li_1, li_2, li_3]:
    li_w = [w_a for w_a in li_0 if li_0.count(w_a) == 1]
    for idx, w in enumerate(li_0):
        if w not in li_w:
            li_0[idx] = 0
for x in range(n):
    print(li_1[x] + li_2[x] + li_3[x])
