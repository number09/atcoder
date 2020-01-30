h = int(input())
l_goukei = list()
counter = 0
while(sum(l_goukei) < h):
    if len(l_goukei) == 0:
        l_goukei.append(1)
    else:
        l_goukei.append(l_goukei[-1] * 2)
print(sum(l_goukei))


