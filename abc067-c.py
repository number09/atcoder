n = int(input())

li_a = list(map(int, input().split()))

sm = sum(li_a)

li_ruiseki = list()

for a in li_a:
    if len(li_ruiseki) == 0:
        li_ruiseki.append(a)
    else:
        li_ruiseki.append(li_ruiseki[-1] + a)

result = -1
for x in li_ruiseki[:-1]:
    a = abs(sm - 2 * x)
    result = min(result, a) if result >= 0 else a

print(result)
