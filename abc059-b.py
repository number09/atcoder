str_a = input()
str_b = input()

int_len = len(str_a) if len(str_a) > len(str_b) else len(str_b)



for x, y in zip(str_a.zfill(int_len), str_b.zfill(int_len)):
    if int(x) > int(y):
        print("GREATER")
        exit(0)
    elif int(x) < int(y):
        print("LESS")
        exit(0)
    else:
        pass
print("EQUAL")

