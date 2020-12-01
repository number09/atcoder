n = int(input())
target = input()
li_w = []
answer = 0
for _ in range(n):
    li_w.append(input())

for w in li_w:
    flg = False
    if target in w:
        answer += 1
        continue
    for start_idx in range(len(w)):
        for kankaku in range(1, len(w)):
            word = ''.join(w[start_idx::kankaku])
            if target in word:
                answer += 1
                flg = True
                break
        if flg is True:
            break
print(answer)
