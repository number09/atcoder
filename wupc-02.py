n = int(input())
s = input()

li_w = s.split('.')
answer = 0
for w in li_w:
    answer += len(w) // 3
print(answer)

