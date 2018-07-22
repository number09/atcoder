str_s = input()

while len(str_s) > 0:
    str_s = str_s[:-1]
    if len(str_s) % 2 == 0:
        spliter = int(len(str_s) / 2)

        if str_s[:spliter] == str_s[spliter:]:
            print(len(str_s))
            exit(0)



