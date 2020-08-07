n = int(input())
li_a = list(map(int, input().split()))

if n % 2 == 1:
    print('error')
    exit(0)

st = -1
answer = 0
for a in li_a:
    if st == -1:
        st = a
    else:
        answer += a - st
        st = -1
print(answer)
