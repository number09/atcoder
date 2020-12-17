t = input()

gu = 0
ki = 0
answer = 0
for i in range(len(t)):
    if i % 2 == 0:
        if t[i:i+2] in ['25', '?5', '2?', '??']:
            gu += 2
        else:
            answer = max(answer, gu)
            gu = 0
    else:
        if t[i:i+2] in ['25', '?5', '2?', '??']:
            ki += 2
        else:
            answer = max(answer, ki)
            ki = 0

print(max(answer, gu, ki))
