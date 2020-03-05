n = int(input())
answer = 0
answer_idx = 0
for i in range(n):
    w = int(input())
    if answer < w:
        answer_idx = i
        answer = w
print(answer_idx + 1)
