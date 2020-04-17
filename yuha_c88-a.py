n = int(input())

answer = list()
for _ in range(n):
    p, q, r = input().split()
    if p[0] == 'B':
        answer.append(r[0])
    elif p[0] == 'M':
        answer.append(r[(len(r)// 2)])
    else:
        answer.append(r[-1])
print(''.join(answer))
