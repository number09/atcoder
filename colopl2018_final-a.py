n = int(input())
s = input()
li_a = s.split('B')

if 'B' not in s:
    k = len(s) * n
    print((k * (k + 1)) // 2)

elif len(li_a[0]) != 0 and len(li_a[-1]) != 0:
    su = 0
    # 端部分の計算
    wk = (len(li_a[0]) + len(li_a[-1]))
    su += sum(range(wk + 1)) * (n - 1)
    su += sum(range(len(li_a[0]) + 1))
    su += sum(range(len(li_a[-1]) + 1))
    # 端以外
    tmp = 0
    for a in li_a[1:-1]:
        if len(a):
            tmp += sum(range(len(a) + 1))
    su += tmp * n
    print(su)
else:
    su = 0
    tmp = 0
    for a in li_a:
        if len(a):
            tmp += sum(range(len(a) + 1))
    su += tmp * n
    print(su)


