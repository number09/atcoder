n = int(input())

li_s = list()

for i in range(n):
    li_s.append(input())

for s in li_s:
    li_w = s.split('okyo')
    if li_w[0] != s:
        wk = "".join(li_w[1:])

        li_w2 = wk.split('ech')
        if li_w2[0] != wk:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

