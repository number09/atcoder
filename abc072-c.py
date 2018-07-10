int_n = int(input())
ar_int_a = list(map(int, input().split()))

st_int_group = set(ar_int_a)
max_count = 0

for i in st_int_group:
    current = ar_int_a.count(i) + ar_int_a.count(i - 1) + ar_int_a.count(i + 1)
    max_count = current if max_count <= current else max_count

print(max_count)




