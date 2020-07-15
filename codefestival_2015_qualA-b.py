n = int(input())
li_a = list(map(int, input().split()))
answer = 0
for idx, v in enumerate(li_a):
    w = n - idx - 1
    answer += v * (2 ** w)
print(answer)
