import fractions

a, b, c, d = map(int, input().split())

# 割り切れる数を探す


left_c = (a - 1) // c
right_c = b // c

c_count = right_c - left_c

left_d = (a - 1) // d
right_d = b // d

d_count = right_d - left_d


lcm_cd = int(c * d / fractions.gcd(c, d))

left_cd = (a - 1) // (lcm_cd)
right_cd = b // (lcm_cd)

cd_count = right_cd - left_cd

print(b - a + 1 - (c_count + d_count - cd_count))

