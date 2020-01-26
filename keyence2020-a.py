h = int(input())
w = int(input())
n = int(input())
sum = 0
answer = 0
while (sum < n):
    if h >= w:
        sum += h
        answer += 1
        w -= 1
    else:
        sum += w
        answer += 1
        h -= 1
print(answer)
