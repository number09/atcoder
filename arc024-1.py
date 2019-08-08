l, r = map(int, input().split())
li_l = list(map(int, input().split()))
li_r = list(map(int, input().split()))
answer = 0
for l in li_l:
    if l in li_r:
        answer += 1
        li_r.remove(l)

print(answer)


