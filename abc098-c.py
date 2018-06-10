# TODO:累積和を使った手法

int_n = int(input())
str_s = input()

changes = 999999

for i in range(int_n):
    member_left = str_s[:i]
    member_right = str_s[i + 1:]
    # print(i)
    # print("left:" + member_left, "right:" + member_right)

    this_change = (member_left.count("W") + member_right.count("E"))

    changes = this_change if (changes >= this_change) else changes

print(changes)



