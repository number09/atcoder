n, s, t = map(int, input().split())

if s == t:
    print(0)
    exit(0)
start_dps = 1
w_s = s
while w_s != 1:
    if w_s % 2 != 0:
        w_s -= 1
    w_s = (w_s // 2)
    start_dps += 1

result_dps = start_dps
li_w = [s]
while result_dps <= n:
    result_dps += 1
    for i in li_w:
        li_next = [i * 2, (i * 2) + 1]
        if t in li_next:
            print(result_dps - start_dps)
            exit(0)
        else:
            li_w = li_next
else:
    print(-1)