n = input()

counter = 0
tmp = ""
for w in n:
    if tmp != w:
        counter = 1
        tmp = w
    else:
        counter += 1
        if counter >= 3:
            print("Yes")
            exit(0)
else:
    print("No")



