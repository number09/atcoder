int_n = int(input())

ar_int_s = list()

for i in range(int_n):
    ar_int_s.append(int(input()))

minused = list()

for i in range(int_n):
    if (sum(ar_int_s) - sum(minused)) % 10 != 0:
        break
    else:
        minused.append(sorted(ar_int_s)[i:i])

print(sum(ar_int_s) - sum(minused))

# 作業中
