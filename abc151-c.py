n, m = map(int, input().split())
li_q = list()
for i in range(m):
    li_q.append(tuple(input().split()))

ac_count = 0
wa_count = 0

s_ac = set()
d_wa = dict()
for l in li_q:
    if l[1] == 'AC':
        if l[0] not in s_ac:
            s_ac.add(l[0])
            ac_count += 1
            wa_count += d_wa.get(l[0], 0)
        else:
            pass
    elif l[1] == 'WA':
        d_wa[l[0]] = d_wa.get(l[0], 0) + 1

print(ac_count, wa_count)
