n = int(input()) - 1
answer = 0

while n > 1:
    for x in range(2, n - 1):
        if n % x == 0:
            break
    else:
        answer += 1
    n -= 1
print(answer)
