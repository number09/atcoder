n, x, y, z = map(int, input().split())
answer = 0
for i in range(n):
    a, b = map(int, input().split())
    if a >= x and b >= y and a + b >= z:
        answer += 1
print(answer)
