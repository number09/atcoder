n = int(input())
li_s = list()

for i in range(n):
    li_s.append(list(input()))

for y in range(n):
    for x in range(n):
        print(li_s[abs(n - 1 - x)][y], end="")
    print("")

