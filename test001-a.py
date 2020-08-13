n = int(input())
s = input()

answer = []

for i in range(1, 5):
    answer.append(s.count(str(i)))
print(max(answer), min(answer))