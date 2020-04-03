n, k = map(int, input().split())
li_t = list()
for _ in range(n):
    li_t.append(int(input()))

li_on = list()
li_off = list()
li_ontime = list()
li_interval = list()

for idx, t in enumerate(li_t):
    if idx == 0:
        li_on.append(t)
        li_off.append(t + 1)
    else:
        if li_off[-1] == t:
            del li_off[-1]
            li_off.append(t + 1)
        else:
            li_on.append(t)
            li_off.append(t + 1)
for idx, on in enumerate(li_on):
    if idx != 0:
        li_interval.append(on - li_off[idx - 1])
if len(li_on) > k:
    add_time = len(li_on) - k
    print(sum([off - on for on, off in zip(li_on, li_off)]) + sum(list(sorted(li_interval)[:add_time])))
else:
    print(sum([off - on for on, off in zip(li_on, li_off)]))

