n, m = map(int, input().split())

# 1の場合
# 2の場合
# 3以上の場合
#  最外でない場合は、9回処理されるので裏返る
#  最外でコーナーの場合は、4回処理されるのでそのまま
#  最外でコーナー以外の場合は、6回処理されるのでそのまま

if n == 2 or m == 2:
    print(0)
elif n ==1 and m == 1:
    print(1)
elif n == 1 or m == 1:
    w = m if n == 1 else n
    print(w - 2)
else:
    print((n - 2) * (m - 2))

