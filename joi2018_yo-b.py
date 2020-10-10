n = int(input())
s_a = "".join(input().split())

answer = 0
for w in s_a.split('0'):
    answer = max(answer, len(w) + 1)
print(answer)