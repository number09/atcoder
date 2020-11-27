n, m = map(int, input().split())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

answer = 0
for a in li_a:
    for b in li_b:
        if a <= b:
            answer += 1
print(answer)
