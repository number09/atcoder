a, b = map(int, input().split())

answer = 0

if (a < 0 and b < 0) or (a > 0 and b > 0):
    answer = abs(a - b)
else:
    answer += (-1 * a) + (b - 1)
print(answer)
