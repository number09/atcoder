n, x = map(int, input().split())

if n == x:
    print(10)
else:
    kouho = [num for num in range(2, 10) if str(num) not in str(x)]
    for k in kouho:
        zyusin_val = 0
        for idx, rs in enumerate(reversed(str(x))):
            zyusin_val += int(rs) * (int(k) ** idx)
        if zyusin_val == n:
            print(k)

