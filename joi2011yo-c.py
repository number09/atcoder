n = int(input())
k = int(input())

li_answer = []

for _ in range(k):
    yoko, tate = map(int, input().split())
    m = min([tate, n - tate + 1, yoko, n - yoko + 1])
    if m % 3 == 0:
        li_answer.append(3)
    elif m % 3 == 1:
        li_answer.append(1)
    else:
        li_answer.append(2)
for a in li_answer:
    print(a)


