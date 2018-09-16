# TODO: case 1 がクリアできていない？

int_h, int_w = map(int, input().split())

li_input = list()

for h in range(int_h):
    li_input.append(list(map(int, input().split())))

# print(li_input)

# 解説より：一筆書きの経路を作る
li_route = list()

for h in range(int_h):
    if h % 2 == 0:
        for w in range(int_w):
            li_route.append((h, w))
    else:
        for w in sorted(range(int_w), reverse=True):
            li_route.append((h, w))

# print(li_route)

for idx, (h, w) in enumerate(li_route[:-1]):
    # print(idx, h, w)
    if li_input[h][w] % 2 == 0:
        pass
    else:
        li_input[h][w] = li_input[h][w] - 1

        (n_h, n_w) = li_route[idx +1]
        li_input[n_h][n_w] = li_input[n_h][n_w] + 1

        print(h + 1, w + 1, n_h + 1, n_w + 1)



