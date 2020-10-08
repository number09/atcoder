n, m = map(int, input().split())
li_n = []
for _ in range(n):
    li_n.append(int(input()))

for k in range(1, m + 1):
    btn_idx = 0
    while True:
        zkn = li_n[btn_idx]
        if li_n[btn_idx] % k > li_n[btn_idx + 1] % k:
            wk = li_n[btn_idx]
            li_n[btn_idx] = li_n[btn_idx + 1]
            li_n[btn_idx + 1] = wk
        btn_idx += 1
        if btn_idx == n - 1:
            break
for l in li_n:
    print(l)