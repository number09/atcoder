n = int(input())
m = int(input())
d_f = {}
answer = set()
for _ in range(m):
    f, t = input().split()
    w_l = d_f.get(f, set())
    w_l.add(t)
    d_f.update({f: w_l})

    w_l_2 = d_f.get(t, set())
    w_l_2.add(f)
    d_f.update({t: w_l_2})

for first in d_f.get('1', set()):
    if first != '1':
        answer.add(first)
        for second in d_f.get(first, set()):
            if second != '1':
                answer.add(second)
print(len(answer))

