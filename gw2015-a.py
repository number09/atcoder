from itertools import combinations

li_q_1 = [25, 39, 51, 76, 163, 111, 136, 128, 133, 138]
li_q_2 = [25, 39, 51, 76, 163, 111, 58, 128, 133, 138]

set_answer = set()
for i in range(len(li_q_1) + 1):
    for com in combinations(li_q_1, i):
        set_answer.add(sum(com))
for i in range(len(li_q_2) + 1):
    for com in combinations(li_q_2, i):
        set_answer.add(sum(com))
for s in sorted(set_answer):
    print(s)
