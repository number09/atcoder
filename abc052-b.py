int_n = int(input())
str_s = input()

int_x = 0
li_x = list()
li_x.append(int_x)
for s in str_s:
    if s == "I":
        int_x += 1
    else:
        int_x -= 1
    li_x.append(int_x)
print(max(li_x))
