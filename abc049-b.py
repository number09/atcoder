int_h, int_w = map(int, input().split())

li_px = list()

for i in range(int_h):
    li_px.append(list(input().split()))

for l in li_px:
    print("".join(l), "".join(l), sep="\n")
