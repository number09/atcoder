int_n, int_k = map(int, input().split())
ar_int_l = list(map(int, input().split()))

print(sum(sorted(ar_int_l, reverse=True)[:int_k]))

