a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


ar = [t % 10 for t in [a, b, c, d, e] if t % 10 != 0]
if len(ar) == 0:
    ar.append(0)
mi = min(ar)


# print(mi)

# print([wt + (10 - (wt % 10)) if wt % 10 != 0 else wt for wt in [a, b, c, d, e]])
w = sum([wt + (10 - (wt % 10)) if wt % 10 != 0 else wt for wt in [a, b, c, d, e]])

if mi > 0:
    w = w - 10 + mi
print(w)
