from collections import defaultdict

int_n = int(input())
ar_int_a = list(map(int, input().split()))

d_cnt = defaultdict(int)
for w in ar_int_a:
    d_cnt[w] += 1


st_int_group = set(ar_int_a)
max_count = 0

for i in st_int_group:
    max_count = max(d_cnt[i] + d_cnt[i - 1] + d_cnt[i + 1], max_count)

print(max_count)




