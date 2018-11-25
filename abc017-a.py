result = 0
for i in range(3):
    score, rate = map(int, input().split())
    result += score * (rate / 10)

print(int(result))
