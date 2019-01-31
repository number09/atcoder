n, m = map(int, input().split())
li_friend = list()

for i in range(m):
    li_friend.append(list(input().split()))

for user in map(str, range(1, n + 1)):
    answer = 0
    for fof in map(str, range(1, n + 1)):
        # 自分自身との判定ならパス
        if user == fof:
            continue
        else:
            # 直接の友達ならパス
            tmp_1 = [user, fof]
            tmp_2 = [fof, user]
            if tmp_1 in li_friend or tmp_2 in li_friend:
                continue

            ls_1 = [x[0] if x[0] != user else x[1] for x in li_friend if user in x]
            ls_2 = [x[0] if x[0] != fof else x[1] for x in li_friend if fof in x]

            if len(set(ls_1).intersection(set(ls_2))) >= 1:
                answer += 1
    print(answer)








