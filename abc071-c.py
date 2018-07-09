int_n = int(input())
ar_int_a = list(map(int, input().split()))

result = []

ar_int_a.sort(reverse=True)

headers = set(ar_int_a)

counters = [{'number': i, 'count': ar_int_a.count(i)} for i in headers
            if ar_int_a.count(i) >= 2]

for i in sorted(counters, key=lambda x: x['number'], reverse=True):

    if len(result) == 0 and i['count'] >= 4:
        print(i['number'] ** 2)
        exit(0)
    elif len(result) < 2:
        result.append(i['number'])
    else:
        break
if len(result) == 2:
    print(result[0] * result[1])
else:
    print(0)










