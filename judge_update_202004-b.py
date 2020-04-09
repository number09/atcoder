n = int(input())
li_pair_red = list()
li_pair_blue = list()

for i in range(n):
    x, c = input().split()
    if c == 'R':
        li_pair_red.append(int(x))
    else:
        li_pair_blue.append(int(x))
for r in sorted(li_pair_red):
    print(r)
for b in sorted(li_pair_blue):
    print(b)


