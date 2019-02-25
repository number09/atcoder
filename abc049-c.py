int_s = input()
str_sr = int_s[::-1]


str_a = ['dream', 'dreamer', 'erase', 'eraser']

str_r = list(map(lambda x: x[::-1], str_a))

result = True

while len(str_sr):
    currnt_flg = False
    for r in str_r:
        # print('r:' + r)
        if len(str_sr) >= len(r) and str_sr[:len(r)] == r:
            # print('ok')
            str_sr = str_sr[len(r):]
            # print(str_sr)
            current_flg = True
            break
    else:
        result = False
        break

if result:
    print('YES')
else:
    print('NO')
