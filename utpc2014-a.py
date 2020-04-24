li_w = input().split()
li_answer = list()
flag = False
for w in reversed(li_w):
    if w != 'not':
        flag = True
        li_answer.append(w)
    else:
        if flag == False:
            li_answer.append(w)
        else:
            if li_answer[-1] == 'not':
                li_answer = li_answer[:-1]
            else:
                li_answer.append(w)
print(' '.join(reversed(li_answer)))



