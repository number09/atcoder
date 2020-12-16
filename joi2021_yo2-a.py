n, a = map(int, input().split())
s = input()

idx_a = a - 1
li_left = []
li_right = []

for idx, w_s in enumerate(s):
    if w_s == '#':
        if idx < idx_a:
            li_left.append(idx + 1)
        elif idx > idx_a:
            li_right.append(idx + 1)
li_right.reverse()

target = 'r'
answer = 0
c_left = len(li_left)
c_right = len(li_right)

while c_left != 0 or c_right != 0:
    if target == 'r':
        if c_right != 0:
            v = li_right[c_right - 1]
            c_right -= 1
        else:
            v = n + 1
        answer += abs(a - v)
        a = v
        target = 'l'
    else:
        if c_left != 0:
            v = li_left[c_left - 1]
            c_left -= 1
        else:
            v = 0
        answer += abs(a - v)
        a = v
        target = 'r'
print(answer)
