n = int(input())
s, t = input().split()

answer = list()
for x, y in zip(s, t):
    answer.append(x + y)

print("".join(answer))
