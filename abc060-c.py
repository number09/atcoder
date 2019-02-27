n, t = map(int, input().split())
li_t = list(map(int, input().split()))

counter = 0

for i in range(len(li_t)):
    if i == (len(li_t) - 1):
        counter += t
    else:
        if li_t[i + 1] - li_t[i] >= t:
            counter += t
        else:
            counter += li_t[i + 1] - li_t[i]


print(counter)
