n, m = map(int, input().split())
li_a = list(map(int, input().split()))

ans = [0] * (m + 1)
for a in li_a:
    ans[a] += 1

for idx, an in enumerate(ans):
    if an > (n // 2):
        print(idx)
        exit(0)
else:
    print('?')


