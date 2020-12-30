n = int(input())
li_ans = []
tmp = n
if n == 0:
    print(0)
else:
    for i in [3, 2, 1, 0]:
        a = tmp // (36 ** i)
        if a < 10:
            li_ans.append(str(a))
        else:
            li_ans.append(chr(65 + a - 10))

        tmp = tmp % (36 ** i)

    print(''.join(li_ans).lstrip('0'))