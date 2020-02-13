n, k = map(int, input().split())
li_p = list(map(int, input().split()))

li_kitai = list()
d_kitai_memo = dict()
for l in li_p:
    if l not in d_kitai_memo:
        val = sum(range(1, l + 1)) / l
        d_kitai_memo[l] = val
        li_kitai.append(val)
    else:
        li_kitai.append(d_kitai_memo[l])

answer = 0
memo = 0
for idx, v in enumerate(li_kitai[:len(li_kitai) - k + 1]):
    if idx == 0:
        memo = sum(li_kitai[idx:idx + k])
    else:
        memo = memo - li_kitai[idx - 1] + li_kitai[idx + (k - 1)]
    answer = max(answer, memo)

print(answer)


