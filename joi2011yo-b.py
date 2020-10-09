import re

word = input()
n = int(input())
li_r = []
answer = 0
ptn = re.compile(word)
for _ in range(n):
    li_r.append(input())

for r in li_r:
    tmp = r
    cn = 0
    for i in range(10):
        if len(re.findall(ptn, tmp)) > 0:
            answer += 1
            break
        tmp = tmp[1:] + tmp[0]
print(answer)

