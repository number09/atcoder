w, h, n = map(int, input().split())
ws = hs = 0

li_point = list()
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        ws = x if x >= ws else ws
    elif a == 2:
        w = x if x <= w else w
    elif a == 3:
        hs = y if y >= hs else hs
    else: # a == r
        h = y if y <= h else h

yoko = w - ws if w - ws > 0 else 0
tate = h - hs if h - hs > 0 else 0

print(yoko * tate)


