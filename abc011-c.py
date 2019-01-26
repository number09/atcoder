import math

n = int(input())
li_ng = list()

for i in range(3):
    li_ng.append(int(input()))

current = n
step = 0

if n in li_ng:
    print("NO")
    exit(0)

w_list = sorted(filter(lambda x: 0 <= x <= n, li_ng), reverse=True)
if len(w_list) == 3 and abs(w_list[0] - w_list[2]) == 2:
    print("NO")
    exit(0)


for ng in sorted(filter(lambda x: 0 <= x <= n, li_ng), reverse=True):
    w_step = (current - ng) // 3  #直近の3の倍数までの処理数
    #print("w_step", w_step)
    if (current - ng) % 3 == 0:
        #一つ前の3の倍数から、-2,-3または-1,-3 とすすむ
        if (current - ng - 2) in li_ng:
            current = current - ((w_step - 1) * 3) - 1 - 3
        else:
            current = current - ((w_step - 1) * 3) - 2 - 3
        step = step + w_step - 1 + 2
    elif (current - ng) % 3 == 1:
        if (current - ng - 2) in li_ng:
            current = current - (w_step * 3) - 2
        else:
            current = current - (w_step * 3) - 3
        step = step + w_step + 1
    else:
        if (current - ng - 1) in li_ng:
            current = current - (w_step * 3) - 1 - 3
            step = step + w_step + 2
        else:
            current = current - (w_step * 3) - 3
            step = step + w_step + 1
    #print(current, step)


if math.ceil(current / 3) + step <= 100:
    #print("yes", math.ceil(current / 3), step)
    print("YES")
else:
    print("NO")




