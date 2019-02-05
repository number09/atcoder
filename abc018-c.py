r, c, k = map(int, input().split())

li_s = list()

answer = 0


def check_zyoge(in_r, in_c, in_range):

    for w in range(in_range):
        if li_s[in_r - w][in_c] == 'x' or li_s[in_r + w][in_c] == 'x':
            break
    else:
        return True

    return False

for i in range(r):
    li_s.append(list(input()))

for tmp_r in range(r):
    for tmp_c in range(c):
        #tmp_r,tmp_cを中央座標とした場合、上下左右にkマス以上あるか確認
        if r - k >= tmp_r >= k - 1 and c - k >= tmp_c >= k - 1:
            if all(map(lambda x: check_zyoge(tmp_r, x, k - abs(tmp_c - x)), [yoko for yoko in range(tmp_c - k +1, tmp_c + k)])):
                answer += 1
        else:
            pass


print(answer)