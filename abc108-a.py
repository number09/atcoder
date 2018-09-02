int_k = int(input())

if int_k % 2 == 0:
    print((int_k // 2) ** 2)
else:
    print((int_k // 2) * ((int_k //2) + 1))