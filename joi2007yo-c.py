s = input()

alph = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

answer = []
for w in s:
    idx = alph.index(w)
    idx -= 3
    if idx < 0:
        idx += 26
    answer.append(alph[idx])

print(''.join(answer))
