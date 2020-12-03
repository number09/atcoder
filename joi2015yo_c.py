h, w = map(int, input().split())
li_we = []

li_answer = []
for _ in range(h):
    li_answer.append([0] * w)

for _ in range(h):
    li_we.append(input())

for h_idx, li in enumerate(li_we):
    last_c_idx = None
    for w_idx, m in enumerate(li):
        if last_c_idx is None:
            if m == '.':
                li_answer[h_idx][w_idx] = -1
            else:
                li_answer[h_idx][w_idx] = 0
                last_c_idx = w_idx
        else:
            if m == '.':
                li_answer[h_idx][w_idx] = w_idx - last_c_idx
            else:
                li_answer[h_idx][w_idx] = 0
                last_c_idx = w_idx
for a in li_answer:
    print(' '.join([str(w_a) for w_a in a]))





