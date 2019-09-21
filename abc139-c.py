n = int(input())
li_h = list(map(int, input().split()))

counter = 0
answer = 0
save = li_h[0]
for i in range(1, n):
    if save >= li_h[i]:
        counter += 1
    else:
        answer = max(answer, counter)
        counter = 0
    save = li_h[i]

print(max(answer, counter))
