n = int(input())
s = input()
li_t = []

for w_s in s:
    li_t = [t for t in li_t if t != w_s]
    li_t.append(w_s)
print(''.join(li_t))