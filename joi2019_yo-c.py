n = int(input())
s = input()

q = []

answer = 0
for w in s:
    q.append(w)
    if len(q) == 2:
        if ''.join(q) in ['XO', 'OX']:
            answer += 1
            q = []
        else:
            q = q[1:]
print(answer)
