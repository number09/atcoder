n = int(input())
li_x = sorted(list(map(int, input().split())))

b = 0
f = n - 1
answer = 0
for idx, x in enumerate(li_x):
    answer += (b - f) * li_x[idx]
    b += 1
    f -= 1
print(answer)


