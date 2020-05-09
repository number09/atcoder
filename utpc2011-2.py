s = input()

num = len(s) // 2

answer = 0
for i in range(num):
    a = i
    d = -(i + 1)
    aw = s[a]
    dw = s[d]

    if aw == '(' and dw == ')':
        pass
    elif aw == ')' and dw == '(':
        pass
    elif aw == dw and not (aw in ['(', ')']):
        pass
    else:
        answer += 1

if len(s) % 2 != 0:
    if not s[num] in ['i', 'w']:
        answer += 1
print(answer)
