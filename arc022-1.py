s = input()
idx_i = 999
idx_c = list()
idx_t = -1

for idx, w in enumerate(s):
    if w.upper() in ["I", "C", "T"]:
        if w.upper() == "I":
            idx_i = min(idx_i, idx)
        elif w.upper() == "C":
            idx_c.append(idx)
        else:
            idx_t = max(idx_t, idx)

if (idx_i != 999 and len(idx_c) != 0 and idx_t != -1) and len([i for i in idx_c if idx_i < i < idx_t]) != 0:
    print("YES")
else:
    print("NO")


