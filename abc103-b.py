str_s = input()
str_t = input()

for i in str_s:
    str_s = str_s[-1] + str_s[0:-1]
    if str_s == str_t:
        print("Yes")
        exit(0)
print("No")


