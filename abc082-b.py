str_s = input()
str_t = input()

str_s_d = sorted(str_s)
str_t_d = sorted(str_t, reverse=True)

if str_s_d < str_t_d:
    print("Yes")
else:
    print("No")
