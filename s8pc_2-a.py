s = input()

wk = ''
answer = 0
for w in s:
    if wk == '':
        if w == 'I':
            wk = 'I'
            answer += 1
        else:
            pass
    else:
        if wk == w:
            pass
        else:
            wk = w
            answer += 1
if wk == 'I':
    print(answer)
else:
    print(answer - 1 if answer > 0 else 0)
