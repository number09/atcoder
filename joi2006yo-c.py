n = int(input())
li_r = []

for _ in range(n):
    li_r.append(input())

main = 1
up = 5
bottom = 2
right = 3
left = 4
rev = 6

answer = 1

for w in li_r:
    if w == 'East':
        main, right, rev, left = left, main, right, rev
    elif w == 'West':
        main, right, rev, left = right, rev, left, main
    elif w == 'Left':
        bottom, right, up, left = left, bottom, right, up
    elif w == 'Right':
        bottom, right, up, left = right, up, left, bottom
    elif w == 'North':
        main, up, rev, bottom = bottom, main, up, rev
    elif w == 'South':
        main, up, rev, bottom = up, rev, bottom, main
    answer += main
print(answer)
