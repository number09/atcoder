n, x = map(int, input().split())
li_l = list(map(int, input().split()))

li_w = [0]

for num in li_l:
    li_w.append(li_w[-1] + num)

print(len(list(filter(lambda y: y <= x, li_w))))

