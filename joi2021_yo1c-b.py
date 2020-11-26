n = int(input())
s = input()

target = 'I' + 'OI' * ((n - 1) // 2)
answer = 0
for w_s, w_t in zip(s, target):
    if w_s != w_t:
        answer += 1
print(answer)
