s = input()
t = input()
answer = 0
for ws, wt in zip(s, t):
    if ws != wt:
        answer += 1
print(answer)
