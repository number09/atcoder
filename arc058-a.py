n, k = map(int, input().split())
li_d = list(input().split())

answer = n

while not all(w not in li_d for w in str(answer)):
    answer += 1

print(answer)
