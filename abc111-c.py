n = int(input())
li_input = list(map(int, input().split()))

li_ki = li_input[0::2]
li_gu = li_input[1::2]


li_ki_counter = sorted([(i, li_ki.count(i)) for i in set(li_ki)], key=lambda x: x[1])
li_gu_counter = sorted([(i, li_gu.count(i)) for i in set(li_gu)], key=lambda x: x[1])


ki_1st = li_ki_counter[0][0]
gu_1st = li_gu_counter[0][0]

if ki_1st == gu_1st:
    # 最頻値が同じ値の場合、2番目に多い要素を使う

    if len(li_ki_counter) == 1:
        ki_2nd = -1
    else:
        ki_2nd = li_ki_counter[1][0]

    if len(li_gu_counter) == 1:
        gu_2nd = -1
    else:
        gu_2nd = li_gu_counter[1][0]

    ptn1 = len(list(filter(lambda x: x != ki_1st, li_ki))) + len(list(filter(lambda x: x != gu_2nd, li_gu)))
    ptn2 = len(list(filter(lambda x: x != ki_2nd, li_ki))) + len(list(filter(lambda x: x != gu_1st, li_gu)))

    if ptn1 >= ptn2:
        print(ptn2)
    else:
        print(ptn1)

else:
    # 最頻値が異なる場合
    print(
        len(list(filter(lambda x: x != ki_1st, li_ki))) +
        len(list(filter(lambda x: x != gu_1st, li_gu)))
    )






