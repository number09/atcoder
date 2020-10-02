n = int(input())
w = 1000 - n
answer = 0
for i in [500, 100, 50, 10, 5, 1]:
    answer += w // i
    w = w % i
print(answer)

