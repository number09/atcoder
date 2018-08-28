int_n, int_m, int_q = map(int, input().split())
li_m = list()
li_q = list()

for m in range(int_m):
    li_m.append(tuple(map(int, input().split())))

for q in range(int_q):
    li_q.append(tuple(map(int, input().split())))

li_answer = [0] * int_q

for idx, (q_start, q_end) in enumerate(li_q):
    for m_start, m_end in li_m:
        if q_start <= m_start and m_end <= q_end:
            li_answer[idx] += 1

for a in li_answer:
    print(a)



