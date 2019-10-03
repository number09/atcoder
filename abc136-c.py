n = int(input())
li_h = list(map(int, input().split()))
save_h = 0
for idx, h in sorted(enumerate(li_h), reverse=True):
    if idx == n - 1:
        save_h = h
    else:
        if h <= save_h:
            save_h = h
        elif (h - save_h) == 1:
            save_h = h - 1
        else:
            print("No")
            exit(0)
else:
    print("Yes")



