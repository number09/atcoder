r, c, k = map(int, input().split())

li_s = list()
for i in range(r):
    li_s.append(list(input()))

answer = 0


li_check_up = list()
for t_r in range(r):
    li_check_up.append([0] * c)
    for t_c in range(c):
        if li_s[t_r][t_c] == 'x':
            pass
        else:
            # r = 0の場合は自分自身の値で判定する
            # r >=1の場合は、上段(r -1) の値 + 1
            if t_r == 0:
                li_check_up[t_r][t_c] = 1
            else:
                li_check_up[t_r][t_c] = li_check_up[t_r - 1][t_c] + 1

li_check_down = [""] * r
for t_r in reversed(range(r)):
    li_check_down[t_r] = ([0] * c)
    for t_c in range(c):
        if li_s[t_r][t_c] == 'x':
            pass
        else:
            # r = r -1 の場合は自分自身の値で判定する
            # 上記以外の場合は、下段(r +1) の値 + 1
            if t_r == (r - 1):
                li_check_down[t_r][t_c] = 1
            else:
                li_check_down[t_r][t_c] = li_check_down[t_r + 1][t_c] + 1


def check_zyoge(in_r, in_c, in_range):

    upcount = li_check_up[in_r][in_c]
    downcount = li_check_down[in_r][in_c]
    if upcount >= in_range and downcount >= in_range:
        return True
    else:
        return False


for tmp_r in range(k - 1, r - k + 1):
    for tmp_c in range(k - 1, c - k + 1):
        # if all(map(lambda x: check_zyoge(tmp_r, x, k - abs(tmp_c - x)), (yoko for yoko in range(tmp_c - k + 1, tmp_c + k)))):
        #    answer += 1
        for yoko in range(tmp_c - k + 1, tmp_c + k):
            if not check_zyoge(tmp_r, yoko, k - abs(tmp_c - yoko)):
                break
        else:
            answer += 1



print(answer)
