r, c, k = map(int, input().split())

li_s = list()

for i in range(r):
    li_s.append(list(input()))

for tmp_r in range(r):
    for tmp_c in range(c):
        #tmp_r,tmp_cを中央座標とした場合、上下左右にkマス以上あるか確認
        if r - k >= tmp_r >= k - 1 and c - k >= tmp_c >= k - 1:
            print(tmp_r, tmp_c)
            print([yoko for yoko in range(tmp_c - k +1, tmp_c + k)])

        else:
            pass


# def check_zyoge(r, c, k):
