import copy

n, k = map(int, input().split())
s = input()


def get_diff(str1, str2):
    return len(list(filter(lambda x: x[0] != x[1], [(s1, s2) for s1, s2 in zip(str1, str2)])))


def get_zan_diff(str1, str2):
    rt = [""] * len(str1)
    wk = list(str2)
    unmatch = list()
    for idx, w_s in enumerate(str1):
        if w_s in wk:
            wk.remove(w_s)
            rt[idx] = w_s
        else:
            unmatch.append(w_s)

    for st in sorted(unmatch):
        for idx, wr in enumerate(rt):
            rt[idx] = st if wr == "" else rt[idx]
    return {"unmatch":len(unmatch), "text":"".join(rt)}


t = list()

save = ""

for i in range(n):

    # 確定していない文字以外で辞書順にならべ、次の候補を取得
    li_wk = sorted(s)
    for w_t in t:
        li_wk.remove(w_t)

    for kouho in li_wk:

        kakutei_kouho = "".join(t) + kouho

        kakutei_kouho_diff = get_diff(kakutei_kouho, s[:len(kakutei_kouho)])

        # 残った文字での判定
        zantext = list(copy.deepcopy(s))
        for d in ("".join(t) + kouho):
            zantext.remove(d)
        zantext = "".join(zantext)

        w_dic = get_zan_diff(s[len(kakutei_kouho):], zantext)

        if w_dic["unmatch"] <= (k - kakutei_kouho_diff):
            t.append(kouho)
            save = w_dic["text"]
            if len(t) == n:
                print("".join(t))
                exit(0)
            break
    else:
        break

print("".join(t) + save)

