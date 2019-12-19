t = int(input())
li_s = list()
for i in range(t):
    li_s.append(input())

for s in li_s:
    answer = 0
    li_tmp = list()
    for w in s:
        li_tmp.append(w)
        if w == 'o' and len(li_tmp) >= 5 and ''.join(li_tmp[-5:]) in ['kyoto', 'tokyo']:
            answer += 1
            li_tmp = list()
    print(answer)

