n, m, x = map(int, input().split())
li_c = []
answer = (10 ** 10) * n
for _ in range(n):
    li_c.append(list(map(int, input().split())))

for w in range(2 ** n):
    st = '{:b}'.format(w)
    li_wk = []
    for idx, y in enumerate(st[::-1]):
        if y == '1':
            li_wk.append(li_c[idx])
    kingaku = [sum([wk[0] for wk in li_wk])]
    li_likai = [sum([wk[w_m] for wk in li_wk]) for w_m in range(1, m + 1)]
    if min(li_likai) >= x:
        answer = min(answer, kingaku[0])
print(answer if answer != ((10 ** 10) * n) else -1)




