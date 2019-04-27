s = input()

# 最初の文字を0にするケース
ptn1 = s[::2].count("1") + s[1::2].count("0")
# 最初の文字を1にするケース
ptn2 = s[::2].count("0") + s[1::2].count("1")

print(min(ptn1, ptn2))

