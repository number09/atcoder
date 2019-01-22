int_r, int_c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
li_map = list()
for i in range(int_r):
    li_map.append(list(input()))

# 4近傍のあきマスを返す
def get_around_space(input_y, input_x):
    li_answer = list()
    for w_y, w_x in ((input_y -1, input_x),(input_y + 1, input_x),(input_y, input_x - 1),(input_y, input_x +1)):
        if 0 <= w_y <= int_r - 1 and 0 <= w_x <= int_c - 1:
            if li_map[w_y][w_x] == ".":
                li_answer.append((w_y, w_x))
    return li_answer


li_queue = list()
li_queue.append((sy - 1, sx - 1))
li_kakutei = list()
li_kakutei.append((sy - 1, sx - 1))
counter = 0
while True:
    counter += 1
    for w_masu in [li_queue.pop(0) for i in range(len(li_queue))]:
        w_list = list(set(get_around_space(*w_masu)))
        for item in [w for w in w_list if w not in li_kakutei]:
            # print(item[0] + 1, item[1] + 1, counter)
            li_kakutei.append(item) # 確定済みリスト
            if item[0] == gy - 1 and item[1] == gx - 1:
                print(counter)
                exit(0)
            li_queue.append(item)

