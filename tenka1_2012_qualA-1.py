n = int(input())

li_w = list()
li_w.append(1)

for i in range(n + 1):
    if i == 0:
        pass
    elif i == 1:
        li_w.append(0)
    else:
        li_w.append(sum(li_w[:-1]))
print(sum(li_w))
