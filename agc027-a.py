n, x = map(int, input().split())
li_a = list(map(int, input().split()))

answer = 0
id = -1

for idx, a in enumerate(sorted(li_a)):
    if x >= a:
        answer += 1
        x -= a
        id = idx
    else:
        break
if answer == 0:
    print(answer)
elif x == 0:
    print(answer)
else:
    if id == (n -1):
        print(answer - 1)
    else:
        print(answer)

