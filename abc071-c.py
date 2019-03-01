import collections

int_n = int(input())
ar_int_a = list(map(int, input().split()))

c = collections.defaultdict(int)
result = []

for a in ar_int_a:
    c[a] += 1

for k in sorted(c.keys(), key=lambda x: x, reverse=True):
    if len(result) == 0 and c[k] >= 4:
        print(k ** 2)
        exit(0)
    elif len(result) < 2 and c[k] >= 2:
        result.append(k)

    if len(result) == 2:
        print(result[0] * result[1])
        exit(0)
else:
    print(0)










