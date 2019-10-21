n = int(input())
s = input()

before = ""
answer = 0
for w in s:
    if w == before:
        pass
    else:
        answer += 1
        before = w
print(answer)

