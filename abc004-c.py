int_n = int(input())

li_num = list(range(1, 7))


# n = 30 毎にもとの列と同じになる
# n = 5　毎に左端を右端に送る動きをする

mod_30 = int_n % 30
div_5 = mod_30 // 5
mod_5 = mod_30 % 5


for i in range(div_5):
    tmp = li_num.pop(0)
    li_num.append(tmp)

for i in range(mod_5):
    idx_1 = i % 5
    idx_2 = idx_1 + 1
    idx_1_val = li_num[idx_1]
    idx_2_val = li_num[idx_2]

    li_num[idx_1] = idx_2_val
    li_num[idx_2] = idx_1_val

print("".join(map(str, li_num)))
