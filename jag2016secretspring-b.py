n, m, t = map(int, input().split())
li_a = list(map(int, input().split()))

pos = 0
li_ans = []
for idx, a in enumerate(li_a):
    if idx == 0:
        li_ans.append(a - m)
    else:
        # 戻るかどうかの判定
        if a - li_a[idx - 1] < (m * 2):
            # 戻らない
            pass
        else:
            # 戻る
            li_ans.append(a - (pos + (2 * m)))
    pos = a

if pos + m <= t:
    li_ans.append(t - (pos + m))
print(sum(li_ans))
