n, a, b = map(int, input().split())

li_d = list()

for i in range(n):
    ew, d = input().split()
    d = int(d)

    if d < a:
        d = a
    elif a <= d <= b:
        pass
    else:
        d = b

    if ew == "West":
        li_d.append(d * -1)
    else:
        li_d.append(d)

out = ""
if sum(li_d) > 0:
    out = "East "
elif sum(li_d) < 0:
    out = "West "

print(out + str(abs(sum(li_d))))
