int_n = int(input())
li_t = list(map(int, input().split()))
int_m = int(input())
li_p = list()
li_x = list()

for i in range(int_m):
    p, x = map(int, input().split())
    li_p.append(p)
    li_x.append(x)


for x, p in zip(li_p, li_x):
    w_li_t = li_t[:]
    w_li_t[x-1] = p

    print(sum(w_li_t))

