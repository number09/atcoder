int_n = int(input())
ar_int_a = list(map(int, input().split()))
ar_int_b = list()
for i in ar_int_a:
    ar_int_b.append(i)
    ar_int_b = ar_int_b[::-1]

print(" ".join(map(str, ar_int_b)))
