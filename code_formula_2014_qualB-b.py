s = input()

r_s = s[::-1]
print(
    sum((int(gu) for gu in r_s[1::2])),
    sum((int(ki) for ki in r_s[::2]))
)
