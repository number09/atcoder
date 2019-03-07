int_n = int(input())

ar_int_s = list()

for i in range(int_n):
    ar_int_s.append(int(input()))


if sum(ar_int_s) % 10 != 0:
    print(sum(ar_int_s))
else:
    li_minus = list(filter(lambda x: x % 10 != 0, ar_int_s))
    if len(li_minus) == 0:
        print(0)
    else:
        print(sum(ar_int_s) - min(li_minus))


