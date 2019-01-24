import itertools

n, k = map(int, input().split())
s = input()


def get_diff(str1, str2):
    return len(list(filter(lambda x: x[0] != x[1], [(s1, s2) for s1, s2 in zip(str1, str2)])))


t = list()

save = ""

for i in range(n):

    # 確定していない文字以外で辞書順にならべ、次の候補を取得
    li_wk = sorted(s)
    for w_t in t:
        li_wk.remove(w_t)
    kouho = li_wk[0]

    kakutei_kouho = "".join(t) + kouho

    kakutei_kouho_diff = get_diff(kakutei_kouho, s[:len(kakutei_kouho)])

    # 残った文字での判定
    li_wk.remove(kouho)

    li_zan_pattern = ["".join(z) for z in itertools.permutations(li_wk)]

    for zp in li_zan_pattern:

        if get_diff(zp, s[len(kakutei_kouho):]) <= (k - kakutei_kouho_diff):
            t.append(kouho)
            save = zp
            if len(li_wk) == 0:
                print("".join(t))
                exit(0)
            break
    else:
        print("".join(t) + save)
        exit(0)

print("".join(t))

