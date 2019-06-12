n = int(input())
s = input()


left_black = 0
right_white = s.count(".")
answer = left_black + right_white

for w in s:
    if w == "#":
        left_black += 1
    else:
        right_white -= 1
    answer = min(answer, left_black + right_white)

print(answer)



