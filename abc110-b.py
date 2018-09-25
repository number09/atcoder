n, m, x, y = map(int, input().split())

li_x = list(map(int, input().split()))
li_y = list(map(int, input().split()))

max_x = max(li_x)
min_y = min(li_y)

# print([z for z in range(x + 1, y + 1)])
# print([zz for zz in range(max_x + 1, min_y + 1)])

if len(set([z for z in range(x + 1, y + 1)]).intersection(set([zz for zz in range(max_x + 1, min_y + 1)]))) > 0:
    print("No War")
else:
    print("War")

