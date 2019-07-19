e = list(input().split())
b = input()
l = list(input().split())
answer = 0

if sorted(e) == sorted(l):
    answer = 1
else:
    w_notin = [lw for lw in l if lw not in e]
    if len(w_notin) == 1 and w_notin[0] == b:
        answer = 2
    else:
        w_in = [lw for lw in l if lw in e]
        if len(w_in) == 5:
            answer = 3
        elif len(w_in) == 4:
            answer = 4
        elif len(w_in) == 3:
            answer = 5
        else:
            pass

print(answer)