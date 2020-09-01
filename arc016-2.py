n = int(input())
li_in = list()
answer = 0
for i in range(n):
    li_in.append(input())

for x in range(0, 9):
    prev = ''
    for l in li_in:
        if l[x] == 'x':
            answer += 1
        if l[x] == 'o' and prev != 'o':
            answer += 1
        prev = l[x]
print(answer)
