import datetime

n = int(input())
li_log = list()

# 入力と前処理のまるめ
for i in range(n):
    start_str = ""
    end_str = ""
    start, end = input().split("-")
    s_time = datetime.datetime(year=2019, month=2, day=28, hour=int(start[:2]), minute=int(start[2:]))
    s_mi = int(start[-1])
    if s_mi % 5 != 0:
        s_time = s_time - datetime.timedelta(minutes=(s_mi % 5))
    start_str = s_time.strftime("%H%M")

    if end >= "2356":
        end_str = '2400'
    else:
        e_time = datetime.datetime(year=2019, month=2, day=28, hour=int(end[:2]), minute=int(end[2:]))
        e_mi = int(end[-1])
        if e_mi % 5 != 0:
            e_time = e_time + datetime.timedelta(minutes=(5 - (e_mi % 5)))
        end_str = e_time.strftime("%H%M")

    li_log.append(start_str + "-" + end_str)

# いもす法の配列
li_check = [0] * ((12 * 24) + 2)

for l in li_log:
    start, end = l.split("-")
    start_h = int(start[:2])
    start_m = int(start[2:])
    start_idx = 12 * int(start_h) + start_m // 5
    li_check[start_idx] += 1

    end_h = int(end[:2])
    end_m = int(end[2:])
    end_idx = (12 * int(end_h) + end_m // 5)
    li_check[end_idx] -= 1


li_result = list()


for i in range(1,len(li_check)):
    li_check[i] += li_check[i - 1]


if li_check[0] >= 1:
    li_result.append("0000")

for i in range(1,len(li_check)):
    if li_check[i] >= 1 and li_check[i - 1] == 0:
        # idxを時刻に逆変換
        li_result.append(format(int(i // 12), "02d") + format(int(i % 12) * 5, "02d"))
    elif li_check[i] == 0 and li_check[i - 1] >= 1:
        li_result.append(format(int(i // 12), "02d") + format(int(i % 12) * 5, "02d"))
    else:
        pass

for i in range(0,len(li_result),2):
    print(li_result[i] + "-" + li_result[i + 1])





