answer = set()
for _ in range(10):
    s = input()
    for idx, v in enumerate(s):
        if v == 'o':
            answer.add(idx)
if len(answer) == 10:
    print('Yes')
else:
    print('No')

