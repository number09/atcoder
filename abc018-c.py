r, c, k = map(int, input().split())

li_s = list()
for i in range(r):
    li_s.append(list(input()))

answer = 0


li_check = list()
for t_r in range(r):
    li_check.append([""] * c)
    for t_c in range(c):
        if li_s[t_r][t_c] == 'x':
            li_check[t_r][t_c] = '0/0'
        else:
            upcount = 0
            # r = 0の場合は自分自身の値で判定する
            # r >=1の場合は、上段(r -1) の値 + 1
            if t_r == 0:
                    upcount += 1
            else:
                upcount = int(li_check[t_r - 1][t_c].split('/')[0]) + 1

            # for up in range(t_r, -1, -1):
            #     if li_s[up][t_c] != 'x':
            #         upcount += 1
            #     else:
            #         break

            downcount = 0
            # r = 0または 一つ冗談がxの場合、素直にループで判定
            # 上記以外の場合は、上段(r -1) の値 - 1
            if t_r == 0 or li_s[t_r - 1][t_c] == 'x':
                for down in range(t_r, r):
                    if li_s[down][t_c] != 'x':
                        downcount += 1
                    else:
                        break
            else:
                downcount = int(li_check[t_r - 1][t_c].split('/')[1]) - 1


            # for down in range(t_r, r):
            #     if li_s[down][t_c] != 'x':
            #         downcount += 1
            #     else:
            #         break

            li_check[t_r][t_c] = str(upcount) + '/' + str(downcount)

# print(li_check)

def check_zyoge(in_r, in_c, in_range):

    upcount, downcount = map(int, li_check[in_r][in_c].split("/"))
    if upcount >= in_range and downcount >= in_range:
        return True
    else:
        return False


for tmp_r in range(r):
    for tmp_c in range(c):
        #tmp_r,tmp_cを中央座標とした場合、上下左右にkマス以上あるか確認
        if r - k >= tmp_r >= k - 1 and c - k >= tmp_c >= k - 1:
            if all(map(lambda x: check_zyoge(tmp_r, x, k - abs(tmp_c - x)), [yoko for yoko in range(tmp_c - k +1, tmp_c + k)])):
                answer += 1
        else:
            pass


print(answer)