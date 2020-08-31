s = input()
t = input()
answer = 0
for i in range(len(s) - len(t) + 1):
    w = s[i:i + len(t)]
    w_match = 0
    for w_t, w_w in zip(t, w):
        if w_t == w_w:
            w_match += 1
    answer = max(answer, w_match)
print(len(t) - answer)

