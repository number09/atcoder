n, x, y = map(int, input().split())

li_a = list(map(int, input().split()))

w_x = x + sum(sorted(li_a, reverse=True)[::2])
w_y = y + sum(sorted(li_a, reverse=True)[1::2])

if w_x == w_y:
    print("Draw")
elif w_x > w_y:
    print("Takahashi")
else:
    print("Aoki")
