n, l = map(int, input().split())
s = input()
tab = 1
crash = 0
for w in s:
    if w == "+":
        tab += 1
    else:
        tab -= 1
    if tab > l:
        crash += 1
        tab = 1
print(crash)




