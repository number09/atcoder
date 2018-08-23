int_s, int_c = map(int, input().split())


if int_s * 2 == int_c:
    print(int_s)
elif int_s * 2 > int_c:
    print(int_c // 2)
else: # int_s * 2 < int_c
    zan_c = int_c - int_s * 2
    print(int_s + zan_c // 4)

