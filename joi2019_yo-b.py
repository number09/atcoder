n = int(input())
li_x = list(map(int, input().split()))
m = int(input())
li_a = list(map(int, input().split()))

for a in li_a:
    idx = a - 1
    target = li_x[idx]
    if target + 1 in li_x or target == 2019:
        pass
    else:
        li_x[idx] += 1
for x in li_x:
    print(x)
