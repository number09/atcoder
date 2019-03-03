int_n = int(input())
ar_int_a = list(map(int, input().split()))
ar_int_b = [-1] * int_n


idx = (int_n // 2)
ar_int_b[idx] = ar_int_a[0]

if int_n % 2 == 0:
    # 偶数
    for i in range(1, int_n):
        if i % 2 == 0:
            idx = idx + i
        else:
            idx = idx + (-1 * i)
        ar_int_b[idx] = ar_int_a[i]
else:
    # 奇数
    for i in range(1, int_n):
        if i % 2 == 0:
            idx = idx + (-1 * i)
        else:
            idx = idx + i
        ar_int_b[idx] = ar_int_a[i]

print(" ".join(map(str, ar_int_b)))
