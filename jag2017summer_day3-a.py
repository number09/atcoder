s = input()

answer = 0
li_w = []
for w in s:
    if w == '(':
        li_w.append(w)
    elif w == ')':
        li_w.pop(-1)
    elif w == '*':
        print(len(li_w))
        exit(0)